"""
函数的作用
    函数就是一段具有独立功能的代码块整合到一个整体并命名，在需要的位置调用这个名称即可完成对应的需求
    函数在开发的过程中可以更高效的实现代码块的重用
函数的使用步骤
    1.定义函数
        def 函数名(参数)：
        代码..........
    2.调用函数
        函数名(参数)
    3.注意
        不同的需求参数可有可无 函数一定要先定义再调用
        如果没有调用函数，函数里面的代码不会执行
        当调用函数的时候，解释器会回到定义函数的地方去执行下方的代码，当定义的函数代码执行完毕后，有回到调用函数的地方然后再向下之行
函数参数的作用
    真实数据的参数为实参 等待接收数据的参数就是形参
    函数中的形参就相当于一个变量
    有了参数就会使代码变得更加灵活
    调用函数的时候形参有几个就要有几个实参
函数返回值作用
    return作用：
        负责函数返回值
        退出当前函数：导致return下方的所有函数不再执行
函数的说明文档
    作用：快速查看函数的作用注释
    help 
        就是查看函数的说明文档(函数的解释说明信息)
        help(函数名） 即可查看函数的说明文档
    定义函数的说明文档
        def 函数名(参数):
            ”“”说明文档“”“ 只有在函数下方的第一行开始才是函数的说明文档
        #def 函数名(参数):
            ”“”不填写任何信息(按回车键)“”“ 回车之后填写说明
函数的嵌套调用：所谓的函数嵌套就是一个函数里面又调用了一个函数

可变参数：
    定义：
        函数的个数不限定
    语法：
        def 函数名（参数1，参数2，*args, **kwargs）：
            函数代码
        *args 表示可变的位置参数  可接收多余的参数
            多余的会以元组的形式保存在args里面
        **kwargs 表示可变的关键字参数 可接收多余的关键字参数
            多余的关键字参数会以字典的形式保存在kwargs里面
    注意：
        当你传递多个参数时，多出来的参数会以元组的形式保存在args里面
        当你传递多个参数时，多出来的参数会以字典的形式保存在kwargs里面

匿名函数lambda：
    作用：
        可以创建一个小型的匿名函数
    语法：
        lambda 参数1，参数2 ：返回值
    应用场景：
        因为匿名函数调用的次数很少
        通常当做另一个函数的参数来使用
几种常见的方法
    1.filter(参数1(参数1是一个返回布尔值的函数),参数2(参数2是一个可迭代的对象))
        作用：
            对可迭代对象进行过滤，得到一个filter()对象，得到的filter得到的对象也是一个可迭代的对象
        语法：
            x = filter(函数，可迭代对象)
        注意：
            Python3.x中filter是一个内置类
            filter 可以给定两个参数，第一个参数是函数，第二个参数是可迭代的对象
            参数函数应该返回的是一个布尔值

    2.map()
        作用:
            让可迭代对象都执行函数里面的操作
        语法：
            x = map(函数，可迭代对象名）
    3.reduce(函数，可迭代对象)
        作用：
            让可迭代对象执行函数里面的操作，得到一个总的数据，返回一个数值
            函数是计算公式
            函数里面需要传递两个参数，让它能够进行计算
        注意：
            Python3.x中reduce()移动到了functools模块里面

Python内置函数总结
    1.数学相关的内置函数
        x = abs(数字) 取绝对值
        x,y = divmod(num1，num2)  求num1除以num2的商和余数
        pow(num,n) 求一个数num的n次方
        round(num,n) 四舍五入保留到指定n位小数
        sum() 用来求和的
    2.可迭代对象相关的
        1.x = all(可迭代对象） 返回一个布尔值
            作用：将数据转换为布尔值 如果可迭代对象里面的元素转换成为布尔值，结果是True，返回结果是True，否则就是False
        2.x = any(可迭代对象） 返回一个布尔值
            作用：将数据转换为布尔值 如果可迭代对象里面的元素转换成为布尔值，结果存在True，返回结果是True，否则就是False
        3.iter(可迭代对象) 获取可迭代对象的迭代器
        4.next() for...in 玄幻的本质就是调用迭代器的next方法
    3.转化相关
        bin(数字) 将数字转换成二进制
        oct（num） 将数字转换成八进制
        hex(num) 将数字转换成十六进制
        chr(字符编码) 将字符编码转换为对应的字符
        ord(字符) 将字符转换成对应的字符编码
    4.变量相关的
        globals 查看所有的全局变量
        locals 查看所有的局部变量
    5.判断对象相关的
        isinstance(对象名，type) 判断一个对象是否是由type这个类创建的
        issubclass(子类名，父类名) 判断一个类是否是由父类创建的
    4.其他
        dir(obj)
            列出一个对象所有的属性和方法
        exit(退出码）
            以指定的退出码结束程序
        open() 用来打开一个文件
        repr() 以字符串的形式保存数据

高阶函数
    定义
        一个函数作为另一个函数的返回值
        一个函数作为另一个函数的参数 最常用的是lambda函数
        在函数内部再定义一个函数

闭包：
    闭包是由函数及其相关的引用环境组合而成的实体（闭包：函数块+引用环境）
    如果一个内部函数里面，对外部作用域（但不是全局作用域）的变量进行引用，那么内部函数就认为是一个闭包
    应用场景：
        1要有函数的嵌套 外部的函数返回内部的函数
        2在外部函数定义了局部变量
        3在内部函数里引用了外部函数中的局部变量
        4那么外部函数的返回值就是一个闭包，即内部函数是一个闭包
    注意：
        在内部函数里面使用外部函数的局部变量
            nonlocal 变量名  这样内部函数就能调用外部函数的局部变量

装饰器：
    语法结构：
        def 装饰器名(fn):
            def inner(相关的参数):
                代码1
                fn(参数)
                代码2
            return inner
        语法结构解释：1.fn是想要装饰的函数 inner()函数与fn()函数有着相同的语法结构 fn有几个参数inner就要写几个参数
                   2.代码1是执行fn函数之前的代码，再执行fn函数，最后执行fn函数后的代码2
                   3.返回的是inner函数
                   4.当再次调用fn函数时，已经不是原来的fn函数，而是返回的inner函数

"""

from functools import reduce


# 定义函数
def first_fun():
    print('hello model')


# 调用函数
first_fun()


# 不同的需求参数可有可无 函数一定要先定义再调用
# 参数的作用
def add_num(num1, num2):
    result = num1 + num2
    print(result)


add_num(7, 8)


# 函数的返回值return作用
def buy():
    return '烟'
    print('ok')


goods = buy()
print(goods)


# 制作一个计算器 计算两数字之和 并保存结果
# 定义函数 有两个参数 返回结果
def sum_num(a, b):
    return a + b


# 输入随机的变量作为函数的实参
# a = int(input('请输入数字1 '))
# b = int(input('请输入数字2 '))
# print(result)
# 函数的说明文档
def sum_num1(a, b):
    """求和函数"""
    return a + b


# 函数说明文档的高级使用
def sum_num2(a, b):
    """

    :param a:参数1
    :param b:参数2
    :return:返回值
    """
    return a + b


help(sum_num1)
help(sum_num2)


# 函数的嵌套调用
# 定义函数2
def test2():
    print('函数2开始....')
    print('函数2运行....')
    print('函数2结束....')


# 定义函数1
def test1():
    print('函数1开始.........')
    # 调用函数2
    test2()
    print('函数1结束.....')


test1()
"""
需求：打印图形
"""


# 打印一条横线
def print_line():
    print('-' * 20)


# 打印多条横线
def sum_line(num):
    for i in range(num):
        print_line()


num = 5
sum_line(num)
"""
需求: 三个数平均值
"""


# 定义求和函数
def sum1(a, b, c):
    return a + b + c


# # 定义求平均值函数
# def avenge():
#     a = int(input('请输入数字1 '))
#     b = int(input('请输入数字2 '))
#     c = int(input('请输入数字3 '))
#     avenge1 = sum1(a, b, c) / 3
#     return avenge1
#
#
# result1 = avenge()
# print(result1)


# 关于可变参数
def add(a=1, b=2, *args):
    result = a + b
    for each in args:  # 多余的参数被写进了args里面以元组的形式存储，是一个可迭代的对象
        result += each
    return f'您输入的{a, b, args}数字的和为{result}'


print(add(2, 4, 3, 4, 7))


# 匿名函数的使用--用另一个函数调用函数
def add1(a, b, fn):
    return fn(a, b)


x3 = add1(5, 7, lambda a, b: a * b)
print(x3)

# filter（）函数的测试
age = [19, 20, 15, 14, 16, 23, 25]
list1 = [
    {'name': 'zhangsan', 'age': 18, 'heiget': 180, 'score': 98},
    {'name': 'lis', 'age': 20, 'heiget': 179, 'score': 97},
    {'name': 'wangwu', 'age': 19, 'heiget': 182, 'score': 96},
    {'name': 'jack', 'age': 21, 'heiget': 185, 'score': 100}
]
x = filter(lambda elf: elf > 18, age)
for i in x:
    print(i, end='\t')
print()
x1 = filter(lambda ele: ele['age'] > 18, list1)
for i in x1:
    print(i)
# reduce的测试
y = reduce(lambda a, b: a * b, age)
print(y)

y1 = reduce(lambda a, b: a + b['age'], list1, 0)
print(y1)


# 高阶函数的使用--将一个函数作为另一个函数的返回值
def foo():
    print('我是foo，我被调用了')
    return bar


def bar():
    print('我是bar，我被调用了')
    return 'hello world'


# 高阶函数--在函数的内部再定义一个函数
def outer():
    def inner():
        print('我是inner函数')
        return 'inner'

    print('我是outer函数')
    return inner


print(foo()())
print(outer()())


# 高阶函数--把函数当做一个函数的参数
def add2(a, b, fn):
    return fn(a, b)


print(add2(1, 2, lambda a, b: a + b))


# --------------------------------装饰器---------------------------------------
# 设定一个装饰jia函数的装饰器
def zsq_jia(fn):  # fn是想要接收的函数
    def inner(a, b):  # inner函数与想要装饰的函数有着相同的结构
        print(f'x的值是{a}，y的值是{b}')
        a += 1
        b += 2
        return fn(a, b) / 2

    return inner


# 设定一个函数
@zsq_jia
def jia(x, y):
    return x + y


print(jia(1, 2))


def zsq_chu(fun):
    def inner(x, y):
        print(x,y)
        return fun(x, y)
    return inner

@zsq_chu
def chu(x, y):
    try:
        z = x / y
    except ZeroDivisionError as e:
        print('除数不能为0')
    else:
        print(z)

chu(1,0)
