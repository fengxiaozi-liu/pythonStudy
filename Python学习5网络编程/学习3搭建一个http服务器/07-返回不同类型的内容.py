from wsgiref.simple_server import make_server
import json


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    response = 'hello'

    # 关于状态码：RESTFUL ==> 前后端分离
    # 2xx:请求响应成功的
    # 3xx:重定向
    # 4xx: 客户端错误 405访问了一个不存在的地址， 405：请求方式不被允许
    # 5xx: 服务器的错误
    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = json.dumps({'name': 'zhangsan', 'age': 18})
    elif path == '/demo':
        with open('test.txt', 'r', encoding='utf8') as file:
            response = file.read(1024)
    elif path == '/hello':
        with open('hello.html', 'r', encoding='utf8') as file:
            response = file.read(1024)
    elif path == '/ajax':
        with open('./11-ajax的使用.html', 'r', encoding='utf8') as file:
            response = file.read()
    elif path == '/data.json':
        with open('data.json', 'r', encoding='utf8') as file:
            response = file.read()
    else:
        status_code = '404 Not Found'
        response = '您找的页面不存在'
    start_response(status_code, [('Content-type', 'text/html;charset=utf8')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    while True:
        httpd = make_server('', 8000, demo_app)
        sa = httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        httpd.handle_request()
