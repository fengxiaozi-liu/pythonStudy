"""
with关键字的后面，需要重写实现__enter__, __exit__两个魔法方法
        当进入with代码块时会自动调用__enter__方法里面的代码
        当with代码块执行完成后自动的调用__exit__方法
语法：
    with class_name() as name1就相当于执行了下面两个方法：
        obj_name = class_name()
        name1 = obj_name.__enter__
        这里的name1为创建对象之后调用__enter__之后的返回值
"""


class Demo:
    def __enter__(self):
        print('__enter__方法被执行')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__str__方法被调用')


with Demo() as d:  # as后面是一个对象名
    # 变量d它是创建的一个对象调用__enter__之后的返回值
    print(d)
