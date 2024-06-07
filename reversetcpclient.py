import socket
import random

def client_program(server_ip, server_port, Lmin, Lmax):
    with open('ascii_file.txt', 'r') as file:
        data = file.read()

    data_length = len(data)
    block_lengths = []

    while data_length > 0:
        block_size = random.randint(Lmin, Lmax)
        if block_size > data_length:
            block_size = data_length
        block_lengths.append(block_size)
        data_length -= block_size

    N = len(block_lengths)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    client_socket.sendall((1).to_bytes(2, byteorder='big') + N.to_bytes(4, byteorder='big'))

    response = client_socket.recv(2)
    response_type = int.from_bytes(response, byteorder='big')
    if response_type != 2:
        print('Error: Did not receive agreement from server')
        client_socket.close()
        return

    reversed_data = []

    offset = 0
    for i, block_size in enumerate(block_lengths):
        block = data[offset:offset + block_size]
        offset += block_size

        client_socket.sendall((3).to_bytes(2, byteorder='big') + block_size.to_bytes(4, byteorder='big') + block.encode('ascii'))

        response = client_socket.recv(2)
        response_type = int.from_bytes(response, byteorder='big')
        if response_type != 4:
            print(f'Error: Did not receive reverseAnswer for block {i+1}')
            client_socket.close()
            return

        length = int.from_bytes(client_socket.recv(4), byteorder='big')
        reversed_block = client_socket.recv(length).decode('ascii')
        reversed_data.append(reversed_block)

        print(f'Block {i+1}: {reversed_block}')

    client_socket.close()

    with open('reversed_file.txt', 'w') as file:
        file.write(''.join(reversed_data))

if __name__ == '__main__':
    # Modify these parameters as needed
    server_ip = '127.0.0.1'  # Localhost or replace with actual server IP
    server_port = 12345       # Replace with actual server port
    Lmin = 5                  # Minimum block size
    Lmax = 15                 # Maximum block size

    client_program(server_ip, server_port, Lmin, Lmax)
