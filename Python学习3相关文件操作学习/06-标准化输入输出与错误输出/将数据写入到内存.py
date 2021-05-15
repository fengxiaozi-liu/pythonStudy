"""
将数据写入到内存涉及到两个类 StringIO 和 BytesIO
StringIO的使用
    语法：
        from io import StringIO
        对象名x = StringIO（）
        方式1：
            x.write(数据)  将数据写入到缓存里面
            x.getvalue() 获取写入的数据
        方式2：
            print(数据，file=x） 将数据打印到内存里面
            print(数据，x.getvalue()) 获取打印在缓存里面的数据

BytesIO的使用
    语法：
        创建一个对象x = BytesIO()
        x.write(数据.encode='utf8') 将数据以二进制的方式写入
        x.getvalue().dencode('utf8‘） 把数据以原有方式获取
"""
from io import StringIO, BytesIO

# 将数据写入到内存里面
s_io = StringIO()
s_io.write('hello ')  # 将数据写入内存缓存起来
s_io.write('world ')  # 将数据写入内存缓存起来

print(s_io.getvalue())

# 将数据打印到内存里面
print('jack', file=s_io)
print('good', file=s_io)
print(s_io.getvalue())

s_io.close()

# 测试BytesIO
b_io = BytesIO()
b_io.write('你好'.encode('gbk'))  # 将文件以二进制写入
print(b_io.getvalue().decode('gbk'))  # 获取数据并解码回原文件
b_io.close()
