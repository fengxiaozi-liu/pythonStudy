"""
文件的读取
    1.open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
        1.python里使用open内置函数打开并操作一个文件
        2.file用来指定打开的文件（是文件的路径，不是文件的名字）
            绝对路径：从电脑盘符开始的路径就是绝对路径
                因为在windows中文件的分隔符是\  而\在Python中是转义字符
                可以进行以下操作来消除转义含义
                1. \\
                2. r'文件地址'
                3.将\换成/
            相对路径：当前文件所在的文件夹开始的路径
                    当前文件是编辑代码所在的文件夹
        3.mode打开文件的模式，默认是r表示只读
            r 只读模式 只能读取不能写入 如果文件不存在会报错
            w 写入模式 打开文件以后只能写入不能读取 如果文件存在会覆盖，如果不存在会新建一个文件
            b 以二进制的形式打开文件  主要是用来操作非文本文件
                rb：以二进制的形式读取
                wb：以为二进制的形式写入
            a 追加模式 如果文件不存在会创建文件 如果文件存在则会追加信息
            r+/w+: 可读写
            t 以文本的形式打开只读
        4.encoding 打开文件时的编码方式
            Windows系统里，默认是gbk
        5.open有一个返回值，打开文件的对象
    2.具体操作
        file_name = open(文件路径（绝对路径，或者相对路径），'需要的读写模式', encoding = 'utf8）
        file_name.read(n) 读取文档的全部数据 指定读取的长度为n
        file_name.readline() 只读取一行的数据
        file_name.readlines() 读取所有行的数据，保存在一个列表里
        file_name.close() 关闭
        注意：
            文档写入时默认utf8写入
            在Windows操作系统中，默认使用gbk编码格式打开文件
    3.关于路径的一些操作
        ../表示返回上一级
            open('../文件地址) 打开上一级的文件
        ./ 表示当前文件夹
            一般是省略
        /
            表示根目录
"""
# 文档写入时默认utf8写入
# 在Windows操作系统中，默认使用gbk编码格式打开文件
# 解决方案：读取和写入使用相同的编码格式
# 用绝地路径打开文件
file = open(r'C:\Users\19693\Desktop\code\Python学习3相关文件操作学习\文件的读写与拷贝\文档.txt', encoding='gbk')
print(file.read().encode().decode())
file.close()
print('-' * 30)
# 用相对路径打开文件
file_name = open('文档.txt', encoding='gbk')
print(file_name.read())
file_name.close()
print('-' * 30)
# 测试w打开文件
file3 = open('文档.txt', 'w+', encoding='gbk')
file3.write('今天的天气不错')
file3.seek(0, 0)  # 光标重置
file3.read()
file3.close()
print('-' * 30)
# 以二进制的方式读取文件
file1 = open('文档.txt', 'rb')
print(file1.read().decode(encoding='gbk'))
file1.close()
print('-' * 30)
# 以二进制的方式写入
file2 = open('文档.txt', 'wb')
file2.write('大家好才是真的好'.encode('utf8'))
file.close()
print('-' * 30)
