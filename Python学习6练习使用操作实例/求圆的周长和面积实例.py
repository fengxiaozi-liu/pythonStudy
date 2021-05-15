"""
定义一个点类
    属性包括横坐标 和 纵坐标
定义一个圆类：
    属性含有圆形和半径
    方法有：
        求圆的周长
        求圆的面颊
        求指定点和圆的关系（圆上，圆内 和 圆外）
"""
import math


class Point:
    """
    这是一个点类 用来生成一个点
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'点({self.x},{self.y})'


class Circle:
    """
    这是一个圆类
    含有计算圆的周长和计算圆面积，判断点与圆位置关系的函数
    """
    def __init__(self, p:Point, radius):
        self.radius = radius
        self.p = p

    def __str__(self):
        return f'一个以{self.p}为圆心，半径长{self.radius}的圆'

    def perimeter(self):
        """
        这是一个求圆周长的方法
        :return: 圆的周长
        """
        circle_perimeter = round(2*math.pi*self.radius, 4)
        return f'圆的周长为{circle_perimeter}'

    def area(self):
        """
        这是一个求圆面积的方法
        :return: 圆的面积
        """
        circle_area = round(math.pi*self.radius**2,4)
        return f'圆的面积为{circle_area}'

    def judge_cp(self, p:Point):
        """
        这是判断一个点是否与创建的一个圆的位置关系的方法
        :param p: 要判断的点
        :return: 圆与点的位置关系
        """
        length_between_points = ((self.p.x - p.x)**2 + (self.p.y - p.y)**2)**0.5
        if length_between_points == self.radius:
            return f'{p}在{self}的圆上'
        elif length_between_points > self.radius:
            return f'{p}在{self}的圆外'
        else:
            return f'{p}在{self}的圆内'


p1 = Point(4, 5)
p2 = Point(10,2)
print(p1, p2)
c1 = Circle(p1, 5)
print(c1)
print(c1.perimeter())
print(c1.area())
print(c1.judge_cp(p2))

