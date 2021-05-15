import socket

# http的服务器都是基于tcp协议的
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip地址只能通过ip地址访问
# sever_socket.bind(('192.168.3.15', 9090))
# # 能够通过127.0.0.1 和 localhost 访问到
# sever_socket.bind(('127.0.0.1', 9090))
# 127.0.0.1和0.0.0.0都表示本机
# 但是0.0.0.0表示所有可用的地址
# 127.0.0.1只能本机访问，其他的不能访问
# 192.168.3.15 可以在局域网之内访问
sever_socket.bind(('0.0.0.0', 8080))
sever_socket.listen(128)
# 接收客户端的信息
# accept 接收一个元组
# 元组的第0个元素是接收的客户端的链接
# 元组的第一个元素是客户端的ip地址和端口号的元组
client_socket, addr = sever_socket.accept()
data = client_socket.recv(1024).decode('utf8')
print(f'接收到的数据{data}')
# 在返回内容之前需要先设置http响应头
# 设置一个响应头就换一行
client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
client_socket.send('content-type:text/html\n'.encode('utf8'))
# 所有的响应头设置完成之后再换行
client_socket.send('\n'.encode('utf8'))
client_socket.send('hello world'.encode('utf8'))