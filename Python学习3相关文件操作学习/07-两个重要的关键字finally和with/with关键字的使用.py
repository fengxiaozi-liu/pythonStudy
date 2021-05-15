"""
with关键字的使用
定义：
    with我们称之为上下文管理器，很多需要手动关闭的链接（exp：文件链接 socket链接 数据库链接 ）都能使用with关键字自动的关闭链接
    注意：
        with关键字的后面，需要重写实现__enter__, __exit__两个魔法方法
        当进入with代码块时会自动调用__enter__方法里面的代码
        当with代码块执行完成后自动的调用__exit__方法
作用：
    with关键字会帮助我们完成那个关闭文件的功能
语法：
    with open('文件路径’，'r') as file_name:
        file.read()
        file.close()不需要写了，with关键字会帮助我们完成这一步操作

"""
# 不使用with关键字打开一个文件
try:
    file = open('../03-文件的读写与拷贝/文档.txt', 'r', encoding='utf8')
except Exception as e:
    print('文件不存在')
else:
    try:
        print(file.read())
    finally:
        file.close()

# 使用with关键字打开一个文件
try:
    with open('文档.txt', 'r') as file1:
        file1.read()

except Exception:
    print('文件不存在')