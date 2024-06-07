# jike222_lxt
### 程序运行说明

#### 环境要求
- Python 3.x
- 操作系统：Windows、Linux 或 macOS

#### 文件结构
确保项目目录中包含以下文件：
```
project_directory/
├── server.py
├── client.py
├── ascii_file.txt
└── README.md (可选)
```
- `server.py`：服务器端程序。
- `client.py`：客户端程序。
- `ascii_file.txt`：包含测试文本的ASCII文件。

#### 创建ASCII文件
创建一个包含全英文可打印字符的ASCII文件 `ascii_file.txt`。
#### 服务器端程序 (`reversetcpserver.py`)

#### 客户端程序 (`reversetcpclient.py`)

### 运行步骤
1. **启动服务器**
    - 在PyCharm中打开并运行 `server.py` 文件。
    - 服务器将在 `0.0.0.0:12345` 监听客户端连接。
2. **启动客户端**
    - 在PyCharm中打开并运行 `client.py` 文件，修改 `server_ip` 和 `server_port` 变量，以匹配服务器的IP地址和端口。

### 配置选项
- **服务器配置：**
  - `server_ip`：服务器的IP地址，默认为 `'0.0.0.0'`。
  - `server_port`：服务器的端口号，默认为 `12345`。
- **客户端配置：**
  - `server_ip`：服务器的IP地址，默认为 `'127.0.0.1'`。
  - `server_port`：服务器的端口号，默认为 `12345`。
  - `Lmin`：发送块的最小长度，默认为 `5`。
  - `Lmax`：发送块的最大长度，默认为 `15`。

### 注意事项
- 确认客户端和服务器可以互相通信。
- 确认网络配置和防火墙设置允许通信。
- 服务器端需要在客户端之前启动。
