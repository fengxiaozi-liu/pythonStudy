"""
sys.stdin 接收用户的输入，可以像input一样接收用户的输入。 和input相关
        sys.stdout 标准输出 修改sys.stdout 可以改变默认的输出位置 读取键盘里的输入数据
            语法：
                sys.stdout = open(file_name,'w', encoding='utf8')  创建数据输出保存的文件
                print(数据） 这时候数据输出的结果就会保存到上面创建好的file_name文件中去
        sys.stderr 错误输出 修改sys.stderr可以修改错误输出的默认位置
            语法：
                sys.stderr = open(file_name,'w', encoding='utf8')  创建数据输出保存的文件
                print(数据） 这时候输出的错误数据就会保存到上面创建好的file_name文件中去
"""
import sys

# 关于sys.stdin的用法
s_in = sys.stdin
while True:
    content = s_in.readline().rstrip('\n')
    if content == '':
        break
    else:
        print(content)

# 关于sys.stdout的用法
sys.stdout = open('stdout.txt', 'w', encoding='utf8')
print('hello ')
print('world ')

# 关于sys.stderr
sys.stderr = open('stderr.txt', 'w', encoding='utf8')
print(1 / 0)