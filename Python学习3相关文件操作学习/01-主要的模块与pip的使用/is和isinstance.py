"""
is 与 isinstance
is运算符 身份运算符
    用来比较是否是同一个对象
    本质是比较两个对象的内存地址 id(obj1) == id(obj2) ?
isinstance
    用来判断一个对象是否是由指定的类（或者父类）创建出来的

issubclass
    判断一个类是否是一个父类的子类
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bar(self):
        print(self.name)

    def add(self, a, b):
        return a + b

    pass


s1 = Student("张三", 18)
s2 = Student("李四", 25)
num1 = [1, 2, 3]
num2 = num1
num3 = [1, 2, 3]

# is的应用
print(num2 is num1)
print(num3 is num1)
print(s1 is s2)
print('-' * 30)
# isinstance
print(isinstance(s1, Student))
print(isinstance(s2, Student))
