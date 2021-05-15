"""
05-异常处理：为了保证程序的健壮性，让编程语言有异常处理机制
    异常：
        在程序运行的过程中，由于编码不规范等造成的程序无法正常执行，此时程序就会报错
    解决方案：
        采用try...except...else...语句进行解决
            作用：
                处理程序运行过程中的异常
            语法使用
                try：
                    异常的代码(你想要测试的这个有没有错误的代码)
                except Exception as e: 如果程序出错了，就会立刻执行except语句
                    当程序出错时候执行的代码
                    e是给异常取的一个变量名
                    Exception是一个大类这里可以换成别的类，处理指定类型的异常 可以用元组来表示处理多个异常的类
                    如果不确定是什么类型的异常可以直接使用Exception
                else:
                    当程序正确时执行的代码
    异常处理的应用场景

"""


# try...except...else...语句的测试

def div(a, b):
    return a / b


try:  # 尝试想要执行的代码
    x = div(5, 2)
except Exception as e:  # 当想要执行的代码出错时执行的代码
    print('除数不能为0')
else:  # 当想要执行的代码正确时
    print(f'结果是{x}')

# 用try...except...else...语句打开一个文件
try:
    file = open('ddd.txt')
    print(file.read())
    file.close()
# e是给异常取的一个变量名  Exception是一个大类这里可以换成别的类，处理指定类型的异常 可以用元组来表示处理多个异常的类
except Exception as e:
    print(e)
    print('出错了')

# # 不采用try...except...else...语句执行用户输入
# age = input('请输入您的年龄')
# if age.isdigit(): 这是可以用正则表达式判断  正则表达式是用来处理字符串的
#     age = int(age)
#     if age > 18:
#         print('您已经成年可以进入本网站')
#     else:
#         print('您的年龄不满18周岁，不能进入这个网站')
# else:
#     print('请输入一个数字')

# 采用try...except...else...语句执行用户输入

age = input('请输入你的年龄')

try:
    age = float(age)
except Exception as e:
    print('请输入数字')
else:
    if age > 18:
        print('您已经成年可以进入本网站')
    else:
        print('你还未成年，不能访问本网站')
