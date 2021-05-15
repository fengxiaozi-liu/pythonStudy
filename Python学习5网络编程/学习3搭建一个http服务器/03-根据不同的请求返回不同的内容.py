import socket

# http的服务器都是基于tcp协议的
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_socket.bind(('192.168.3.15', 8085))
sever_socket.listen(128)
while True:
    client_socket, addr = sever_socket.accept()
    data = client_socket.recv(1024).decode('utf8')  # 浏览器发送过来的数据有可能是空的
    path = '/'
    if data:
        path = data.splitlines()[0].split(' ')[1]
        print(f'请求的路径{path}')
    # 响应头
    response_header = 'HTTP/1.1 200 OK\n'  # 200状态码是登录成功了
    # 响应体
    response_body = 'hello world'
    if path == '/login':
        response_body = '欢迎来到登录页面'
    if path == '/register':
        response_body = '欢迎来到注册页面'
    elif path == '/':
        response_body = '欢迎来到首页'
    else:
        # 页面未找到 返回404状态码
        response_header = 'HTTP/1.1 404 Page Not Found\n'
        response_body = '您的页面未找到'
    # 响应头
    response_header += 'content-type:text/html;charset=utf8\n'
    response_header += '\n'
    response_all = response_header + response_body
    client_socket.send(response_all.encode('utf8'))
