import socket

# 创建一个基于 udp 的网络socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口号和ip地址
s.bind(('192.168.3.15', 9090))
# recvfrom接收数据 recvfrom是一个阻塞的方法，等待
content = s.recvfrom(1024)
# 接收到的数据是一个元组，元组里面是第0个是接收到的数据，第1个是发送者的ip地址和端口号
content1 = content[0].decode('utf8')
address = content[1][0]
duankou = content[1][1]
print(f'从{address}的地址，端口号是{duankou}接收到了{content1}')
s.close()