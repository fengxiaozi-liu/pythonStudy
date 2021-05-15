"""
python对象中方法相关的知识点
方法的概念：
    描述目标的行为动作
    和函数相似：1都封装了一系列的行为动作
             2都可以被调用执行一系列的动作
             3和函数最主要的区别是：调用方式的不同
方法的划分：
    实例方法：默认第一个参数接收一个实例
        class 类名：
            def 方法名（参数/self,想要添加的参数，.....）：
                相关代码
        调用：
        标准调用：实例（对象）名.实例方法
        其他调用：类调用 间接调用 （本质都是找到函数本身来调用）
    类方法：默认第一个参数接收到一个类
        class 类名:
            @classmethod
            def 类方法名(类参数(cls)，第二个参数,....)
                相关的代码块
        查看类方法： Ctrl + 鼠标左键点击 classmethod
        调用：
        标准调用：1类名.类方法名(参数)
                2通过类创建的实例.类方法名(参数)
        其他调用：间接调用
    静态方法：第一个参数什么也不接收
        class 类名:
            @staticmethod
            def 静态方法名(参数1，参数2，。。。。。)
                相关的代码块
        调用
            标准调用：类名.静态方法名（参数） 或者是实例名.静态方法名（参数）
            其他调用：间接调用
    注意：1划分的依据是：方法的第一个参数要接收的数据类型
        2不管是哪一种方法都是存储在类当中，没有在实例当中的
        3不同类型的调用方法不同 保证一个原则：第一个接收的参数是相关方法想要的数据
    使用：
        语法
        不同类型方法的规则
        不同类型方法的调用
        根据不同的问题，决定设计什么样的方法来解决问题
    不同类型的方法访问不同类型的属性
        1实例方法可以访问类属性可以访问实例属性
        2类方法只能访问类属性
        3静态方法可以直接访问类和实例
补充
    类
        元类：创建类对象的类 最终的元类是type7
        类的创建方式和流程
            1表象创建
                通过class 类名 创建
            2手动创建
                通过元类type创建
                想要接收这个类的变量名 = type(类名,(想要继承的父类),{类中的相关属性和方法(要用字典的形式保存)})
            3类的创建流程（可以限制类的拦截，且在不同的模块作用的范围不同）
                1先检测自己类对象中是否有明确的__metaclass__属性
                2再检测父类中是否存在__metaclass__属性
                3再检测模块中是否存在__metaclass__属性
                4最够通过内置的type的元类进行创建
    类的描述
        目的:方便我们自己理解逻辑关系
            方便和别人交流
            方便生成项目文档
        描述方式：见下方实例
        生成项目文档（涵盖所有有用的模块）
            生成项目文档的方式 1使用内置函数pydoc具体步骤如下
                                1打开Windows自带的cmd窗口
                                2找到文件的所在路径
                                3.1输入 python -m pydoc -p 指明的相关端口号（需要指定的端口号）
                                3.2输入 python -m pydoc -b 模块名称（不需要端口号）
                                3.3输入 python -m pydoc -w 模块名称（创建一个网页）
                           2查看文档的描述
                           3启动本地服务
"""


# 函数和方法的调用区别
# 函数的调用
def eat():
    print(1, end=' ')
    print(2, end=' ')
    print(3, end='\n')


eat()


# 方法的调用
class Person:
    # 实例方法 self这个参数是一个实例
    def eat2(self):
        print(1, end=' ')
        print(2, end=' ')
        print(3, end='\n')
        print('这是一个实例方法', self)

    # 类方法
    # 查看类方法 Ctrl + 鼠标左键点击 classmethod
    @classmethod
    def leifangfa(cls):
        print('这是一个类方法', cls)

    # 静态方法
    @staticmethod
    def jingtaifangfa():
        print('这是一个静态方法')


p = Person()
p.eat2()
Person.leifangfa()
Person.jingtaifangfa()
# 实例方法调用参数错误会报错
# Person.eat2()
# 验证三大方法存储在类的字典里面
print(Person.__dict__)
p.age = [1, 2, 3]
print(p.__dict__, '没有方法')


# 实例方法的相关内容
class Test1:
    # 实例方法增加相关的参数
    def eat3(self, food):
        print(f'我想要吃{food}')

    def eat4(xxx):
        print(xxx)


t1 = Test1()
# 实例方法不需要调用第一个参数self，直接调用第二个参数
t1.eat3('土豆')
# 访问类中的相关函数
print(Test1.eat3)
# 通过类调用实例方法 123是实例，蔬菜是另一参数
Test1.eat3(123, '蔬菜')
# 间接调用
func = Test1.eat3
func(1, '肉')
# 测试用实例调用实例方法不写
t1.eat4()


# 类方法的相关内容
class Test2:
    @classmethod
    def lff(cls, num):
        print('类方法', cls, num)


# 通过类调用类方法
Test2.lff(3)
# 通过实例调用
t2 = Test2()
t2.lff(6)
# 间接调用类方法
func1 = Test2.lff
func1(123)


# 通过衍生类调用类方法
class A(Test2):
    pass


A.lff(2)


# 静态方法相关的内容
class Test3:
    @staticmethod
    def jtff(num):
        print('这是一个静态方法', num)


# 通过类调用静态方法
Test3.jtff(3)
# 通过实例调用静态方法
t3 = Test3()
t3.jtff(5)
# 通过间接调用静态方法
func2 = Test3.jtff
func2(7)


# 测试不同类型的方法访问不同类型的属性
class Person:
    age = 0

    # 实例方法访问不同的属性
    def shilifangfa(self):
        print(self)
        # 实例方法访问类属性
        print(self.age)
        # 实例方法访问实例（对象）属性
        print(self.num)

    # 类方法访问不同的属性
    @classmethod
    def leifangfa(cls):
        print(cls)
        # 类方法访问类属性
        print(cls.age)

    @staticmethod
    def jingtaifangfa():
        print(Person.age)
        print(p.num)


p = Person()
p.num = 10
# 验证实例方法访问不同属性
p.shilifangfa()
# 验证类方法访问不同的属性
Person.leifangfa()
# 验证不同的方法访问不同的属性
p.jingtaifangfa()
# 验证元类
num = 10
# 数字所属的类
print(num.__class__)
# 数字类的元类
print(num.__class__.__class__)


class Money:
    pass


m = Money()
# 实例的上部分是一个类
print(m.__class__)
# 类的上部分是一个元类
print(Money.__class__)


# 通过type元类创建类
def run(self):
    print(self)


Dog = type('Dog', (), {'count': 0, 'run': run})
dog1 = Dog()
print(dog1.count)
print(Dog.__dict__)


# 类的描述
class People:
    """
    关于类的描述，类的作用，类的构造函数，类的属性描述
    """
    count = 1

    def run(self, distance, step):
        """
        关于方法的描述作用效果是什么
        :param distance:参数的含义，参数的类型，参数的默认值
        :param step:
        :return:返回结果的含义 返回数据的类型
        """
        print('人在跑')


help(People)
