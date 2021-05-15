"""
多态
    定义：
        1一个类所延伸的多种形态
        2调用的多种形态：
            在继承的前提下，使用不同的子类调用父类相同的方法，产生不同的功能
    多态在Python中的体现：
        鸭子类型：动态类型的一种风格，只要一个对象会走，会叫，会游泳，那他就可以当做一个鸭子来处理，关注点在于对象的行为和属性
                而非对象的类型
        所以在Python中没有真正意义上的多态也不需要多态
"""


# ------------------------------------------多态----------------------------------------------


class Animal:
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
