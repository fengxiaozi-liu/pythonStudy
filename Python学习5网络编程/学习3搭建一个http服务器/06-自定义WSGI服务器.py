from wsgiref.simple_server import make_server


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
        response = '欢迎你到test页面'
    elif path == '/demo':
        response = '欢迎来到demo页面'
    else:
        status_code = '404 Not Found'
        response = '您找的页面不存在'
    start_response(status_code, [('Content-type', 'text/html;charest=utf8'), ('ssss', 'ddd')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.handle_request()
