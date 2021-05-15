"""
定义三个类小狗，小猫，人
小狗姓名 年龄（默认一岁）  吃饭，睡觉，看家（格式：名字xxx，年龄是xx岁的小狗在xx
小猫：姓名，年龄（默认一岁） 吃饭，睡觉，玩，捉老鼠（格式：名字是xx，年龄是xx岁的小猫在捉老鼠
人：
    姓名，宠物，吃饭，玩，睡觉（格式名字是xx，年龄是xx岁的人在xx
    养宠物（让所有的宠物吃饭睡觉玩）
    让宠物工作（让所有的宠物根据自己的职责开始工作）
"""


class Pet:
    def __init__(self, age=1):
        self.age = age
        self.list1 = ['吃饭', '睡觉', '玩']


class Dog(Pet):
    def __init__(self, name='大黑'):
        super().__init__()
        self.name = name
        self.list2 = self.list1
        self.list2.append('看家')

    def __str__(self, key=1):
        return f'名字是{self.name},年龄是{self.age}的小狗在{self.list2[key]}'

    def dahei(self):
        print('大黑去看家了')


class Cat(Pet):
    def __init__(self, name='小花'):
        super().__init__()
        self.name = name
        self.list3 = self.list1
        self.list3.append('捉老鼠')

    def __str__(self, key=1):
        return f'名字是{self.name},年龄是{self.age}的小猫在{self.list3[key]}'

    def xiaohua(self):
        print('小花去捉老鼠了')


class Person(Dog, Cat):
    def __init__(self, name='小明', age=1):
        self.name = name
        self.age = age
        self.list1 = ['吃饭', '睡觉', '玩', '养宠物']

    def __str__(self, key=1):
        return f'名字是{self.name}的，年龄是{self.age}的人，在{self.list1[key]}'


p = Person()
d = Dog()
c = Cat()
print(p.__str__(2))
print(d)
print(c)
p.dahei()
p.xiaohua()
