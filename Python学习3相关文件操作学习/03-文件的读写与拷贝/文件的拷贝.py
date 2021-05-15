"""
文件拷贝是将一个文件的数据读取出来再写入另一个文件
"""
import os

old_file_name = input('请输入你想要拷贝的文件的文件路径 ')
if os.path.isfile(old_file_name):
    old_file = open(old_file_name, 'rb')
    name = os.path.splitext(old_file_name)
    new_file_name = name[0] + 'bak' + name[1]
    new_file = open(new_file_name, 'wb')
    while True:
        content = old_file.read(1024)
        new_file.write(content)
        if not content:
            break
    old_file.close()
    new_file.close()
