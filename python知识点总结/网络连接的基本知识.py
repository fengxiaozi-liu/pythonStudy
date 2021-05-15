socket
	利用socket可以让不同网络之间的进程实现通信
	socket一般有两个参数
	socket.scoket(AddressFamily, Type)
	AddressFamily中包括
		AF_INET 用于不同电脑之间的通信
		AF_UNIX 用于同一台电脑之间的通信
	Type套接字也有两种不用类型
		SOCK_STREAM 用于tcp协议
		SOCK_DGRAM 用于udp协议

	利用socket建立udp协议
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 建立一个连接对象
		s.bind(('127.0.0.1',8000)) 绑定地址和端口号
		data, address = s.recvfrom(1024) 接收数据
			data是拿到的数据
			address是拿到ip地址和端口号
		s.sendto(数据.encode('utf8')，('ip地址'，8000)) 向指定的端口号发送数据
		s.close

	利用socket建立tcp协议
		tcp客户端
			s = socket.sockt(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(('ip地址',端口号)) 和指定的服务端建立连接
			s.send(数据.encode('utf8')) 向服务端发送数据
			s.recv(1024).decode('utf8') 从服务端拿到接收到的数据
			s.close() 关闭连接
		tcp服务端
			s = socke.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind(('ip地址'，端口号)) 服务端绑定ip地址和端口号
			s.listen(128) 服务端监听请求数据
			client_data, client_address = s.accept() 接收客户端发来的数据
				client_data 里面含有请求的所有数据，包括请求头和请求体等
				client_address 里面函数发送请求的ip地址和端口号
			if 对client_data进行处理
				client_data.send(数据) 服务端向客户端发送数据
					数据里面包括响应头和响应体
WSGI
	是一种网络协议，任何一种自定制的socket连接必须遵守的协议

wsgiref
	是一种服从WSGI协议的定制的socket连接
	from wsgiref.simple_server import make_server
	def run_server(environ, start_response)
		path = enivron['PATH_INFO'] 
			environ中是请求相关的所有信息，里面有请求头和请求体
		if 判断path
			start_response(status, [('Content-Type', 'text/html;charset=utf8')]) 向客户端发送响应头
				其中status是状态码
				[()]列表里面存储元组数据，每一个元组都是响应头的信息
			return [bytes(response_body,encoding='utf8')] 向客户端发送响应体
			return [response_body,] 发送中一定要用字节的形式

	if __name__==__main__:
		httpd = make_server('',8000, run_server函数)
		httpd.server_forever

多线程与多进程
	多线程
		多线程的创建和使用
			x = threading.Thread(targer=函数，name=给这个子线程命名)
			x.start() 开始启动这个线程
		多线程机制
			开启多线程后，多个线程同时共享一个数据，对数据的修改几乎是同步的，因此要加上一个互斥锁
		互斥锁
			lock = threading.Lock() 建立一个互斥锁对象
			lock.acquire() 开启互斥锁，当一个线程进来之后，后面的线程不能进入
			lock.relase() 关闭互斥锁等到互斥锁关闭之后，后面的线程可以进来
		队列
			q = quene.Quene() 创建一个队列
			q.put(x) 将数据放到队列里
			q.get(x) 将数据从队列里面取出
	多进程 
		多进程的创建和使用
		x = multiprocessing.Process(target=函数名,name=进程名，arg=(x,))
		x.start()
	进程和线程的区别
		进程： 进程是让不同程序之间同时运行
		线程： 线程是让同一程序之间的不同任务同时进行
		


