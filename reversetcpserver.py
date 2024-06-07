import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            msg_type = client_socket.recv(2)
            if not msg_type:
                break
            msg_type = int.from_bytes(msg_type, byteorder='big')

            if msg_type == 1:  # Initialization
                N = int.from_bytes(client_socket.recv(4), byteorder='big')
                client_socket.sendall((2).to_bytes(2, byteorder='big'))
            elif msg_type == 3:  # reverseRequest
                length = int.from_bytes(client_socket.recv(4), byteorder='big')
                data = client_socket.recv(length).decode('ascii')
                reversed_data = data[::-1].encode('ascii')
                client_socket.sendall((4).to_bytes(2, byteorder='big') + len(reversed_data).to_bytes(4, byteorder='big') + reversed_data)
        except:
            break

    client_socket.close()

def server_program():
    server_ip = '0.0.0.0'
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f'Server listening on {server_ip}:{server_port}')

    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connection from {addr}')
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    server_program()
