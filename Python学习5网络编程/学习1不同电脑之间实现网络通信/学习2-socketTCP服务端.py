import socket,os

# 创建一个socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.3.15', 9090))
s.listen(128)  # 把socket变成一个别动监听的socket
client_socket, client_addr = s.accept()  # 接收客户端的请求
data = client_socket.recv(1024).decode('utf8')
if os.path.isfile(data):
    with open(data, 'r', encoding='utf8') as file:
        content = file.read()
        client_socket.send(content.encode('utf8'))
else:
    client_socket.send('文件不存在'.encode('utf8'))

