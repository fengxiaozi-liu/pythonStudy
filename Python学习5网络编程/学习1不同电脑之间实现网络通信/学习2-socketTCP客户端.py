import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = open('demo.txt', 'r')
data = input('请输入你想要拿到的文件名 ')
s.connect(('192.168.3.15', 9090))
s.send(data.encode('utf8'))

content = s.recv(1024).decode('utf8')
with open(data, 'w', encoding='utf8') as file:
    file.write(content)
s.close()
