import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.3.15', 9090))


def send_msg():
    while True:
        msg = input('傻子\n')
        s.sendto(msg.encode('utf8'), ('192.168.3.15', 8000))
        if msg == 'exit':
            break


def recv_msg():
    while True:
        data, addr = s.recvfrom(1024)
        msg = data.decode('utf8')
        print(f'{msg}')


# 创建两个能够同时进行的线程
t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)

t1.start()
t2.start()