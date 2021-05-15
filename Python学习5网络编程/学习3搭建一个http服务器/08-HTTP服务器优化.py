from wsgiref.simple_server import make_server
import json


def load_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileNotFoundError as e:
        print('文件未找到')


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    response = 'hello'
    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = json.dumps({'name': 'zhangsan', 'age': 18})
    elif path == '/demo':
        response = load_file('test.txt')
    elif path == '/hello':
        response = load_file('hello.html')
    else:
        status_code = '404 Not Found'
        response = '您找的页面不存在'
    start_response(status_code, [('Content-type', 'text/html;charset=utf8'), ('ssss', 'ddd')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.handle_request()
