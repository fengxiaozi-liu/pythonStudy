"""
属性相关的主题：
    私有化属性：1Python中没有真正的私有化支持，但是，可以使用下划线完成伪私有的效果
             2类属性（方法）和实例属性（方法）遵循相同的规则
             x：公有属性 支持{1类内部方法2子类内部访问3模块内部其他位置访问4.1import形式导入4.2from模块import*形式导入}
            -y：受保护的属性 支持{1类内部的访问2子类内部的访问3模块内部的其他位置访问}
            __z 私有属性 支持{类内部的访问}
                私有化属性机制：名字重整 重改为_类名__变量名 （所以在访问__变量名的时候访问不到,名字被修改了)
                             目的：防止外界的直接访问
                                  防止子类的同名称属性覆盖
            应用场景 数据保护
                   数据过滤
    只读属性
        只能读取不能写入
        应用场景
            有些属性只限内部根据不同的场景进行修改，而对外界来说，不能修改，只能读取（比如电脑的网速，网络状态的属性）
            方式1：通过公开的方法 优化
                1先私有化属性2通过方法公开3使用property来优化（property的作用是以使用属性的方式来使用方法）
                补充：经典类：没有继承自（object）
                     新式类：继承自（object）
                     property 在新式类中的用法是:
                     方式1
                     class C(object):
                        def getx(self): return self._x
                        def setx(self, value): self._x = value
                        def delx(self): del self._x
                        x = property(getx, setx, delx, "I'm the 'x' property.")
                     方式2
                     class C(object):
                        @property
                        def x(self):
                            "I am the 'x' property."
                            return self._x
                        @x.setter
                        def x(self, value):
                            self._x = value
                        @x.deleter
                        def x(self):
                            del self._x
            方式2：
                通过setattr函数设置只读属性：setattr（当增加或者修改一个实例属性的时候就会自动的调用这个函数）
                    def __setattr__(self,key,value):
                        # 判定key是否是我们要设置的指定的只读属性
                        if key == 属性名 and key in self.__dict__.keys():
                        # 如果不是只读属性就添加到实例属性里面去
                        else:
                            self.__dict__[key] = value
    内置特殊属性
        类属性
            __dict__  类的属性
            __bases__ 类的所有父类构成的元组
            __doc__ 类的文档字符
            __module__ 类定义所在的模块
        实例属性
            __dict__ 实例的属性
            __class__实例对应的类
"""


# 私有化属性
class Animal:
    # 类属性且是共有属性
    x = 10
    # 受保护的属性
    _y = 12
    __z = 15

    def test(self):
        print(self.x)
        print(self._y)
    # print(self.__z)


class Dog(Animal):
    def test1(self):
        print(Dog.x)
        print(self.x)
        print(Dog._y)
        print(self._y)

    # print(Dog.__z)
    # print(self.__z)


# 测试代码
# 类内部访问测试公有化属性 受保护的属性 私有化属性
a = Animal()
a.test()
# 通过衍生的子类访问测试公有化属性 受保护的属性 私有化属性
d = Dog()
d.test1()
# 通过模块的其他部分访问
# 父类访问
print(Animal.x)
# 派生类访问
print(Dog.x)
# 父类实例访问
print(a.x)
# 子类实例访问
print(d.x)
# 跨模块访问测试
b = 66
# 测试其他模块访问受保护的属性
# 父类访问
print(Animal._y)
# 派生类访问
print(Dog._y)
# 父类实例访问
print(a._y)
# 子类实例访问
print(d._y)
# 跨模块访问测试
_c = 55
# 测试名字重整
print(Animal.__dict__)
print(Animal._Animal__z)


# 数据保护和数据过滤


class Person:
    # 数据保护
    # 初始化方法 主要作用：当我们创建一个实例对象之后会自动的调用这个方法来初始化这个对象
    def __init__(self):
        self.age = 18
        self.__age1 = 20

        # 设置修改私有化属性

    def SetAge(self, value):
        # 数据过滤
        if isinstance(value, int) and 0 < value < 200:
            self.__age1 = value
            return self.__age1
        else:
            print(f'您输入的数据{value}有错误')


p1 = Person()
print(p1.age)
print(p1.__dict__)
p2 = Person()
p2.age = 19
print(p2.age)
# 修改私有化属性操作
print(p1.SetAge(20))
# 测试数据过滤
print(p1.SetAge(201))
print(p1.SetAge('abc'))


# 方式1使属性变成只读属性
class People:
    def __init__(self):
        # 私有化属性
        self.__age = 55

    # 公开的方法
    @property  # 主要的作用是可以以使用属性的方式，来使用这个方法
    def getAge(self):
        return self.__age


p3 = People()
# 测试读取私有化属性
# print(p3.getAge())
# 测试property
print(p3.getAge)


# 新式类和经典类

# 新式类


class Person1:
    pass


print(Person1.__bases__)


# Python2.x版本中如果定义一个类，没有显示的继承自object，那么这个类就是一个经典类
# 必须显示object才是一个新式类
# Python3.x如果定义一个类就是一个新式类，隐式继承object

# property在新式类和经典类中的使用方法


class Person2(object):
    def __init__(self):
        self.__age = 10

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    age = property(get_age, set_age)


p4 = Person2()
print(p4.age)
p4.age = 18
print(p4.age)
print(p4.__dict__)


# 第二种使用方式


class Person3:
    def __init__(self):
        self.__age = 19

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age


p5 = Person3()
print(p5.age)
p5.age = 55
print(p5.age)
print(p5.__dict__)


# 方式2设置只读属性


class Person4:
    # 当我们通过实例.属性 = 值，给一个实例增加一个属性，或者说修改一下属性值得时候都会调用这个方法
    # 在这个方法的内部，才会真正的把这个属性以及数据存储到__dict__ 这个字典里面
    def __setattr__(self, key, value):
        print(key, value)

        # 判定key是否是我们只读属性的名称
        if key == 'age' and key in self.__dict__.keys():
            print('这个属性是只读属性，不能设置数据')
        # 如果不是只读属性，真正的给它添加到实例里面去
        else:
            self.__dict__[key] = value


p6 = Person4()
p6.age = 18
p6.name = 'sz'
print(p6.age)
p6.age = 999
print(p6.__dict__)


# 类的内置属性


class Person5:
    """
    这是一个人
    """

    def __init__(self):
        self.age = 18

    def run(self):
        print('run')


p7 = Person5()
# 测试类的各个内置属性
print('下面是dict')
print(Person5.__dict__)
print('下面是base')
print(Person5.__bases__)
print('下面是doc')
print(Person5.__doc__)
print('下面是module')
print(Person5.__module__)
# 测试实例的内置属性
print(p7.__dict__)
print(p7.__class__)
