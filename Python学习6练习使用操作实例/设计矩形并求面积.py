"""
设计两个类 点类 和 矩形类
点类属性包括x，y
矩形类属性包括左上角和右下角的点
矩形类行为，能够计算矩形的面积
          能够判断一个点是否在矩形的内部
"""


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, left_point: Point, right_point: Point):
        self.left_point = left_point
        self.right_point = right_point

    # 创建一个计算矩形面积的函数
    def calculated_area(self):
        length = self.right_point.x - self.left_point.x
        width = self.left_point.y - self.right_point.y
        area = 0
        area += length * width
        return area

    # 创建一个传入的点是否在矩形内的方法
    def judge(self, p: Point):
        if self.left_point.x <= p.x <= self.right_point.x:
            if self.right_point.y <= p.y <= self.left_point.y:
                return True
            else:
                return False
        else:
            return False


# 创建两个点对象
p1 = Point(4, 20)
p2 = Point(30, 8)
# 创建一个矩形对象
r1 = Rectangle(p1, p2)
# 计算这个矩形的面积
print(r1.calculated_area())
# 判断一个传入的点是否在矩形内部
# 先创建一个要判断的点
p3 = Point(3, 18)
print(r1.judge(p3))
