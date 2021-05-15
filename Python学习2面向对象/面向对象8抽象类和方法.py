"""
抽象类：
    一个抽象出来的类，并不是一个具体的类
    不能直接创建实例的类，否则会报错
抽象方法：
    抽象出来的一个方法
    不具备具体实现 不能直接调用 子类不实现会报错
Python中的体现
    无法直接支持需要借助一个模块
        import abc
    设置类的元素
        abc.ABCMeta
    使用装饰器装饰对应的方法
        @abc.abstractmethod
    注意：
      子类如果继承的是父类的抽象方法，那么必须实现在父类中的所有抽象方法
"""
import abc


class Animal(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def jiao(self, word):
        print(f'{word}会叫')


class Dog(Animal):
    def jiao(self):
        super().jiao('狗')
        print('汪汪汪')


class Cat(Animal):
    def jiao(self):
        super().jiao('猫')
        print('喵喵喵')


def test(obj):
    obj.jiao()


d = Dog()
c = Cat()
test(c)
a = Animal()
a.jiao('动物')
