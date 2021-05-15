"""
系统的内置异常
    ZeroDivisionError  除数不能为0的异常
    FileNotFoundError 文件不存在的异常 exp: open('xxx.txt)
    FileExitsError 文件已经存在的异常 exp: os.mkdir 多次创建同名的文件夹
    ValueError  值得错误 exp: int('hello')
    KeyError   键的错误
    SyntaxError 语法错误
    IndexError 脚标错误

自定义抛出异常
    定义一个自己的异常：
        class MyError(Exception): 注意：一定要继承Exception类来重写__init__,__str__方法
            def __init__(self,参数1，参数2）：
                代码区域
            def __str__(self):
                return 当错误是打印的信息
    调用自己定义的异常：
        raise MyError(参数）

"""


# 要求：让用户输入用户名和密码，如果用户名和密码在6~12位正确，否则不正确


class MyError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'长度要在{self.x}到{self.y}之间'


password = input('请输入您的密码 ')
if 6 <= len(password) <= 12:
    print('密码正确')
else:
    # print('密码不正确')
    # 使用raise关键字抛出一个异常
    raise MyError(6,12)
