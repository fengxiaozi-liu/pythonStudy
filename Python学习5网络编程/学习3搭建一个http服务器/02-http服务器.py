import socket

# http的服务器都是基于tcp协议的
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sever_socket.bind(('192.168.3.15', 9090))
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
client_socket.send(addr[0].encode('utf8'))
"""
接收到的数据GET / HTTP/1.1  
    GET是请求的方式 
    /   /后面是请求的路径以及请求的参数
    HTTP/1.1  是http使用的版本号
Host: 192.168.3.15:9090
    Host是请求的服务器地址
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63
    User-Agent是用户代理，最开始设计的目的是为了能从请求头辨识浏览器的类型
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
"""
