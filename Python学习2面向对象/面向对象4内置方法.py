"""
方法相关的补充：
私有化方法：
    def __方法名（self）：
        相关的代码块
内置特殊方法：
    生命周期方法
    其他内置方法{信息格式化
                      __str__ 格式化相关的方法 返回给用户看的字符串 __str__ 方法的调用：print(对象名)
                      __repr__ 返回地址及相关的属性给编程人员看 __repr__方法的调用：print(repr(对象名))
               调用操作
                    __call__使得’对象‘具备相当的函数，求调用的能力 __call__方法的调用：对象名(有参数传递相关的参数，不计个数)
               索引操作
                    作用：可以对一个对象进行索引操作
                    调用__setitem__ 对象名.字典名['key'] = 数据
                       __getitem__ 对象名.字典名['key']
                       __delitem__ del 对象名.字典名['key']
               切片操作
                    作用：对一个对象实现切片操作
                    调用__setitem__ 对象名.列表名[key] = value
                       __getitem__ 对象名.列表名[key]
                       __delitem__ del 对象名.列表名[key]
               比较操作
                    作用：可以自定义对象‘比较大小，相等以及真假的规则’
                    调用：相等 __eq__
                         不相等 __ne__
                         小于 __lt__
                         大于 __gt__
                         小于等于 __le__
                         大于等于 __ge__
                    补充：
                        可以通过@functool.total_ordering 来补全相关的比较操作
                        上下文环境中__bool__ 可以自己设定 默认为非空为真
               迭代器（遍历操作）
                    怎么样可以让我们自己创建的对象可以使用for in 进行遍历
                        实现__getitem__方法
                        实现__iter__方法
                    怎么样让我们自己创建的对象可以使用next的函数访问
               描述器:可以描述一个属性的操作对象
                    定义方式1property
                          2封装相关的属性
                    调用细节：
                        用实例进行操作 可以调用set get delete
                        用类进行操作只能操作 get
                        不能够顺利转换的场景1新式类和经典类的差异
                                        2方法拦截{1一个实例的正常访问顺序：1实例对象对自己的字典进行访问
                                                                    2再访问对应类的字典
                                                                    3如果有父类访问父类的字典
                                                                    4还没有找到就会调用__getattr__方法
                                                2如何做到优先访问描述器的__get__方法：1查看是否实现了__get__方法，如果有就优先访问
                                                                                2没有，就按照属性的访问顺序进行执行
                描述器的种类：
                    资料描述器 实现了 get set 方法是资料描述器
                    非资料描述器 仅仅实现了get方法就是非资料描述器
                    资料描述器 > 实例属性 > 非资料描述器
                   }
"""

# 私有化方法
import functools


# 实现一个描述器
class SetBianLiang:
    def __get__(self, instance, owner):
        return instance.w
        print('get')

    def __set__(self, instance, value):
        instance.w = value
        print('set')

    def __delete__(self, instance):
        del instance.w
        print('del')


@functools.total_ordering
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        # 对象的索引操作
        self.cache = {}
        # 对象的切片操作
        self.list1 = []
        # 遍历操作
        self.result = 1

    # 内置函数__str__
    def __str__(self):
        return f'这个人的名字是{self.name},这个人的年龄是{self.age}'

    # 内置函数__repr__
    # def __repr__(self):

    # 内置函数call方法啊
    # 类似于偏函数的使用方法
    # 偏函数：我来指明一个函数里面的某一个参数去偏爱某一个数值之后所产生的一个新的函数
    def __call__(self, *args, **kwargs):
        print('call方法', args, kwargs)

    # 内置函数__setitem__索引操作
    # 对象的增/改一个元素操作
    def __setitem__(self, key, value, ):
        self.cache[key] = value
        self.list1[key] = value

    # 对象的查找一个元素操作
    def __getitem__(self, item):
        # 字典的索引操作
        return self.cache[item]

        # __getitem__ 的遍历操作
        # self.result += 1
        # if self.result >= 6:
        #     raise StopIteration
        # return self.result

    # 对象的删除一个元素操作
    def __delitem__(self, key):
        del self.cache[key]
        del self.list1[key]

    # 内置函数的比较操作
    def __eq__(self, other):
        return self.age == other.age

    # 内置函数大于的操作
    def __gt__(self, other):
        print(self.age, other.age)
        return self.age > other.age

    # 内置函数的小于操作
    def __lt__(self, other):
        return self.age < other.age

    # 内置函数__iter__实现遍历操作
    def __iter__(self):
        return self

    # 内置函数__next__
    def __next__(self):
        for key in self.__dict__.keys():
            if key == 'height':
                raise StopIteration

    # 实现一个描述器
    w = SetBianLiang()


p = Person('张三', 18, 180)
p1 = Person('lisi', 25, 175)
# 测试内置函数__str__
print(p)
# 测试__repr__
print(repr(p))
print('-' * 30)

# 测试call方法
p(123, 4, name='sz')
print(p.__dict__)
print('-' * 30)

# 测试相关的索引操作
# 测试__setitem__
p.cache['name'] = 'xiaohua'
# 测试__getitem__
print(p.cache['name'])
# 测试__delitem__
del p.cache['name']
print('-' * 30)

# 测试切片操作
p.list1.extend([1, 2, 3, 4, 5, 6])
p.list1[0:4:2] = [5, 6]
p.list1.append(10)
print(p.list1)
print('-' * 30)

# 测试比较操作
print(p == p1)
print(p != p1)
print(p > p1)
print(p < p1)
print('-' * 30)

# __getitem__的遍历操作
# for i in p:
#     print(i)

# __iter__ , __next__实现遍历操作
for each in p:
    print(each)
print('-' * 30)


# 实现一个描述器
class People:
    age = SetBianLiang()


p2 = People()
p2.age = 18
print(p2.age)
print(p2.__dict__)

"""
补充偏函数的相关知识
需求：
创建很多的画笔
画笔的类型(铅笔，钢笔)
画笔的颜色（红 黄 青 绿）
"""


def creatPen(p_color, p_type):
    print(f'创建一一个{p_type}类型的画笔，他的颜色是{p_color}')


# 创建一个偏函数钟爱钢笔
print('-' * 30)
penfunc = functools.partial(creatPen, p_type='钢笔')
# 调用创建的偏函数传递的参数是一一对应的
penfunc('红色')


# 通过call方法创建
class PenFactory:
    def __init__(self, p_type):
        self.p_type = p_type
        self.dict1 = {}
        self.num = 2

    # 通过call创建偏函数
    def __call__(self, color):
        print(f'创建一一个{self.p_type}类型的画笔，他的颜色是{color}')

    def __str__(self):
        return f'创建了一个{self.p_type}类型的画笔，颜色待定'

    def __iter__(self):
        return self

    def __next__(self):
        for key in self.__dict__.keys():
            if key == 'dict1':
                raise StopIteration('stop')
        print(self.dict1)


# 创建一个实例
pen1 = PenFactory('铅笔')
# 调用call方法
pen1('绿色')
print(pen1)
pen1.dict1['name'] = 'xiaohua'
print(pen1.dict1)
print(pen1.__dict__)
for one in pen1:
    print(one)
