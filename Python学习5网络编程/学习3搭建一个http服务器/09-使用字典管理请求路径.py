from wsgiref.simple_server import make_server
import json


def load_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileNotFoundError as e:
        print('文件未找到')


def show_test():
    return load_file('test.txt')


def demo():
    return json.dumps({'name': 'zs', 'age': 18})


def show_hello():
    return load_file('hello.html')


def index():
    return '欢迎来到首页'


url = {'/hello': show_hello, '/test': show_test, '/': index, '/demo': demo}


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    status_code = '200 OK'

    method = url.get(path)
    if method:
        response = method()
    else:
        status_code = '404 Not Found'
        response = '您找的页面不存在'
    start_response(status_code, [('Content-type', 'text/html;charset=utf8'), ('ssss', 'ddd')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8080, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.handle_request()
