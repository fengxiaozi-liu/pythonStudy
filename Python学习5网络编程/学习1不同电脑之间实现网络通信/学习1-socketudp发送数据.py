"""
socket
    不同的电脑之间实现通信
        ip地址可以标识网络中的主机，而传输层的协议+端口可以卫衣标识主机的用用程序（进程）。这样利用ip地址、协议、和端口就可以标识网络的进程
        网络中的进程通信可以利用这个标志与其他进程进行交互
    什么是socket：
        进程间通信的一种方式，可以让不同的进程之间实现通信
    创建：
        import socket
        socket.socket(Address Family,Type)
        函数socket.socket可以创建一个socket 该函数有两个参数
        Address Family 可以选择AF_INET（用于internet进程通信）或者AF_UNIX(用于同一台机器进程间的通信)
        Type 套接字类型，可以是SOCKET_STREAM（流程套接字，主要用于TCP协议）或者SOCKET_DGRAM（数据报套接字，用于UDP）
"""
import socket

# 关于SOCKET
# 1.创建socket并连接
# 第一个参数AF_INET表示socket用来进行网络连接
# 第二个参数SOCK_DGRAM 表示进行一个UDP连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2.发送数据
# data：要发送的数据
# address：发给谁参数是一个元组，元组里有两个元素 一个是ip地址一个是端口号
s.sendto('下午好'.encode('utf8'), ('192.168.3.15', 9090))
# 3. 关闭socket
s.close()
