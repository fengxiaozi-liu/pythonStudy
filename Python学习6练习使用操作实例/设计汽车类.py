"""
设计一个汽车类Auto
汽车类中含有轮胎个数，汽车颜色，车身重量，速度等
汽车类中含有的行为有加速，减速，停车
再定义一个小类CarAuto，添加空调和cd属性
并且实现方法的覆盖操作
覆盖的方法有加速和减速
"""


class Auto:
    """
    这是一个所有汽车的父类
    """

    def __init__(self, car_color: str, car_weight, car_speed, car_tires=4):
        self.car_color = car_color
        self.car_weight = car_weight
        self.car_speed = car_speed
        self.car_tires = car_tires

    def speed_up(self, n):
        """
        这是汽车添加速度的函数
        :param n: 汽车想要加多少速度
        :return: 加速后汽车的速度
        """
        if self.car_speed >= 120:
            print('您的汽车已经超速，不建议加速')
        else:
            self.car_speed += n
            return self.car_speed

    def speed_down(self, n):
        """
        汽车的减速函数
        :param n: 汽车想要减少的速度
        :return: 汽车减速后的速度
        """
        if self.car_speed <= 0:
            print('汽车处于停止状态，不需要减速')
        else:
            self.car_speed -= n
            return self.car_speed

    def stop_car(self):
        """
        这是一个停下来汽车的操作
        :return: 汽车已经停止的提示
        """
        if self.car_speed == 0:
            print('汽车处于停车状态，不需要再次停车')
        else:
            self.car_speed = 0
            return '汽车已经停下来了'


class CarAuto(Auto):
    def __init__(self, air_condtion: str, cd: str, car_color, car_weight, car_speed, car_tires=4):
        super(CarAuto, self).__init__(car_color, car_weight, car_speed, car_tires)
        self.air_condtion = air_condtion
        self.cd = cd

    def __str__(self):
        return f'这个车的颜色是{self.car_color},车重{self.car_weight}kg,空调是{self.air_condtion},正在播放cd{self.cd}' \
               f'以{self.car_speed}km/s的速度行驶'



    def speed_up(self, n):
        """
        这是汽车添加速度的函数
        :param n: 汽车想要加多少速度
        :return: 加速后汽车的速度
        """
        if self.car_speed >= 120:
            print('您的汽车已经超速，不建议加速')
        else:
            self.car_speed += n
            return self.car_speed

    def speed_down(self, n):
        """
        汽车的减速函数
        :param n: 汽车想要减少的速度
        :return: 汽车减速后的速度
        """
        if self.car_speed <= 0:
            print('汽车处于停止状态，不需要减速')
        else:
            self.car_speed -= n
            return self.car_speed


c1 = CarAuto('格力', '笨小孩', '黄色', 200, 80)
c2 = CarAuto('奥克斯', '起风了', '黑色', 200, 90)
print(c2)
print(c1)
print(c1.car_color)
print(c1.speed_up(10))
