"""
设计一个宠物店类：
    宠物店类含有：
        属性：店名 店中的宠物[使用列表存储宠物]
        方法：展示所有宠物的信息
宠物狗类：
    属性：昵称 性别 年龄 颜色
    狗会： 叫 拆家 吃饭
宠物猫类
    属性 昵称 性别 颜色 眼睛的颜色
    猫会：叫 撒娇 吃饭
"""


class Pets:
    """
    这是一个总的宠物类，里面包含宠物的名字 性别 年龄的属性
    还有宠物 吃饭 叫的一般方法
    """

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self):
        """
        这是一个宠物吃饭的方法
        :return: 什么宠物正在吃饭
        """
        return f'{self.name}正在吃饭'

    def shout(self):
        """
        这是一个宠物叫的方法
        :return: 什么宠物在叫
        """
        return f'{self.name}会叫'


class Dogpets(Pets):
    def __init__(self, name, gender, age, color):
        super(Dogpets, self).__init__(name, gender, age)
        self.color = color

    def tear_down(self):
        """
        这是一个某一个小狗宠物拆家的方法
        :return: 某一只狗在拆家
        """
        return f'{self.name}会拆家'

    def shout(self):
        """
        这是一只小狗在汪汪叫的方法
        :return: 具体哪一只小狗在汪汪叫
        """
        return f'{self.name}在汪汪叫'


class Catpets(Pets):
    def __init__(self, name, gender, age, eyes_color):
        super(Catpets, self).__init__(name, gender, age)
        self.eyes_color = eyes_color

    def coquettish(self):
        """
        这是小猫在撒娇的方法
        :return: 具体哪一只小猫在喵喵叫
        """
        return f'{self.name}正在撒娇'

    def shout(self):
        """
        这是一只小猫在叫的方法
        :return: 具体哪一只小猫在叫
        """
        return f'{self.name}在喵喵叫'


class Petshop:
    def __init__(self, name):
        self.name = name
        self.shop_pets = []

    def __str__(self):
        return f'欢迎来到{self.name}宠物店'

    def add_pets(self, pet: (Dogpets, Catpets)):
        """
        这是一个将具体的宠物加入到宠物店中的方法
        :param pet: 来自猫类或者是狗类的一个具体对象
        :return:宠物店的所有宠物
        """
        self.shop_pets.append(pet)
        return self

    def show_pets(self):
        """
        这是查看宠物店宠物信息的方法
        :return: 每一只宠物的具体信息
        """
        for each in self.shop_pets:
            if isinstance(each, Dogpets):
                print(each.name, each.gender, each.age, each.color)
            else:
                print(each.name, each.gender, each.age, each.eyes_color)


# 创建两个具体的狗实例
d1 = Dogpets('大黄', '公', 3, '白色')
d2 = Dogpets('大黑', '母', 2, '黑色')
# 创建两个具体的猫实例
c1 = Catpets('小花', '母', 1, '棕色')
c2 = Catpets('Tom', '公', 2, '蓝色')
# 创建一个具体的宠物店
s1 = Petshop('宠物天堂')
print(s1)
s1.add_pets(d1).add_pets(d2).add_pets(c1).add_pets(c2)
s1.show_pets()

