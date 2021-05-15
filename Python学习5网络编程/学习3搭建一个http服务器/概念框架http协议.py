"""
需要：
    自己手动搭建一个网站
    要求：
        在浏览器里面输入192.168.3.15:9090能够看到内容
http协议：
    概念：
        http(Hypertext Transfer Protocol)协议全称超文本传输协议
    作用：
        用来传输超文本
        超文本：HTML(HyperTextMarkupLanguage)
        HTML: 超文本标记语言
        C/S架构:client-server 手机淘宝上的app
        B/S架构:browser-server 使用浏览器访问淘宝
客户端和服务端
    request headers 请求头
        接收到的数据GET / HTTP/1.1
            GET是请求的方式
            /   /后面是请求的路径以及请求的参数
            HTTP/1.1  是http使用的版本号
        Host: 192.168.3.15:9090
            Host是请求的服务器地址
    response headers 响应头
        在返回内容之前要设置一个响应头
        每写一个响应头就要换行
        等到所有的响应头书写完毕后也要换行
ip地址的绑定：
    127.0.0.1：端口号
        本机能访问，其他人访问不到
    0.0.0.0：端口号
        表示本机的所有可用的ip地址
        本机能够访问，其他人也能够访问
    c类ip地址：端口号
        访问这个地址需要这个完整的ip地址和端口号

WSGI服务器：
    底层实现创建一个socket服务器
        from wsgiref.simple_server import make_server
        if __name__ == '__main__':
            httpd = make_server('', 8000, demo_app)
                其中demo_app是一个函数
                def demo_app(environment,start_response)
                    start_response('200 ok',[('Content-Type','text/html;charset=utf8')])
                        自动调用的方法,第一个参数是执行码，第2个参数是请求头
                    return [data.encode('utf8')]
                        返回的是一个浏览器显示的内容
                demo_app需要两个参数
                第0个参数表示环境（电脑的环境，请求路径相关的环境）
                    environment是客户端返回过来的许多数据，这些数据保存在一个字典中
                    其中重要的一个是PATH_INFO能够获取到用户的访问路径
                第1个参数是一个函数，用来返回响应头
                这个函数需要一个返回值返回值是一个列表
                这个列表里面只有一个元素，是一个二进制，表示返回给浏览器的数据
            sa = httpd.socket.getsockname()
            print("Serving HTTP on", sa[0], "port", sa[1], "...")
            import webbrowser
            webbrowser.open('http://localhost:8000/xyz?abc')
                这段代码的作用是打开电脑的浏览器，并且在浏览器里输入http://localhost:8000/xyz?abc
            httpd.handle_request()
                只处理一次请求然后退出程序

于状态码：RESTFUL ==> 前后端分离
    2xx:请求响应成功的
    3xx:重定向
    4xx: 客户端错误 405访问了一个不存在的地址， 405：请求方式不被允许
    5xx: 服务器的错误
"""
