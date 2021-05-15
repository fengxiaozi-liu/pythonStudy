"""
面向对象三大特性之封装
封装：将一些属性和方法封装在一个对象当中，对外是隐藏内部具体实现细节。
    优点：
        使用更加的方便
        保证数据的安全
        有利于代码维护
继承：
    概念
        一个类‘拥有’另一个类的‘资源’方式之一
        拥有：指的是使用权
        资源：指的是非私有的属性和方法
    目的：
        方便资源重用
    分类：
        单继承
            一个类仅仅继承类一个父类
        多继承
            一个类继承了多个父类

    继承下的影响：
        继承的资源
            Python中，继承是指，资源的使用权
            所以，测试某个资源是否被继承，其实是测试子类当中能补不能访问到父类的资源
            结论：除了私有的属性和方法其他的都能使用，包括共有属性方法，受保护属性和方法，内置方法
        资源的使用
            1继承的几种形态
                单继承
                无重叠的多继承
                有重叠的多继承
            2几种形态应该遵循的标准原则
                单继承：
                    从下往上的原则访问属性和方法
                无重叠的多继承
                    单调原则：先去左侧继承链去找，再去右侧的继承链去找
                有重叠的多继承
                    从上往下的原则找，碰到相同位置的再从左向右的位置去找
            3针对于几种标准原则的方案演化
                深度优先
                    概念：沿着一个继承链，尽可能往深了去找
                    具体步骤：
                        1把根节点压入栈中
                        2每次从栈中弹出一个元素，搜索所有在它下一级的元素，把这些元素压入栈中
                        3重复第二个步骤直到结束为止
                    问题：
                        在‘有重叠的多继承’当中违背了‘重写可用’的原则
                广度优先
                    概念：
                        沿着继承链，尽可能宽了去找
                    具体算法：
                        1把根节点放到队列的末尾
                        2每次从队列的头部取出一个元素，查看这个元素的下一级元素，把他们放到队列的末尾
                        3重复上面的步骤
                c3算法
                    步骤：
                        两个公式：L(object) = [object]
                                L(子类(父类1，父类2)) = [子类] + merge(L(父类1),L(父类2),[父类1，父类2])
                        注意： + 代表合并列表
                              merge算法：1第一个列表的第一个元素是后续列表的第一个元素或者在后续列表中没有出现
                                        则将这个元素合并到最终的解析列表中并从当前操作的所有列表中删除
                                        2如果不符合，则跳过此元素查找下一个列表的第一个元素，重复1的判断规则
                                        3如果最终无法把所有的元素归并到解析列表，则报错
                    注意：
                        c3算法不是拓扑排序算法
                        拓扑排序步骤：
                            1找到入度为0的节点
                            2输出这个节点并且删除这个节点，然后删除这个节点的出边
                            3重复上面的步骤
                Python各个版本遵循的算法
                    Python2.2之前的版本采用
                        采用算法：
                            深度优先
                        问题：
                            容易造成重写不可用的问题
                    Python2.2版本
                        出现了经典类和新式类：
                            经典类采用深度优先算法
                            新式类采用改进的深度优先算法（在出栈中采用以后优先的原则，后面出栈的类在前面有则删除前面出栈的类）
                        新式类改进的深度优先的问题：
                            无法识别错误的继承关系
                    Python2.3-2.7版本：
                        经典类：
                            采用深度优先算法
                        新式类：
                            采用c3算法
                    Python3.x版本
                        删除经典类只存在新式类：
                            新式类中采用c3算法
                查看类的继承链：
                    方式1：
                        import inspect
                        inspect.getmro(想要查看的类)
                    方式2：
                        想要查看的类名.__mro__
                    方式3：
                        想要查看的类名.mro()
        资源的覆盖
            概念：
                优先级高的会比优先级高的先调用（被叫做资源的覆盖或者是资源重写）
            包括：
                属性的覆盖
                方法的重写
            原理：
                优先级高的类写了一个和优先级低的类相同的资源（属性或者方法）
                到时候去获取资源就会优先选择优先级比较高的类的资源而摒弃优先级低的资源
                这个现象就叫做资源的覆盖
            注意事项：
                当调用优先级比较高的资源时，注意self，cls的变化
                    谁调用的返回的就是谁
                        exp：A类调用B类的方法 返还的是A类
                            A类创建的对象调用b类的方法，返还的self是A类创建的对象
        资源的累加
            概念：
               在一个类的基础上增加一个额外的资源
               子类相比于父类，多一些自己特有的资源
               在覆盖的方法基础上，新增内容
            新增内容：
                方案1：
                    类名.__init__(self)
                方案2：
                    在低优先级的方法中，通过‘super’调用高优先级的方法
                        概念：super是一个类 只能在新式类中有效
                        作用：起代理的作用，帮我们完成沿着MRO链条找到下一级的节点去调用相应方法的任务
                        问题：
                           沿着谁的MRO链条 沿着参数2的MRO链条
                           找到谁的下一个节点 找到参数1的下一个节点
                           如何应对类方法，静态方法，实例方法的传参问题
                        语法原理
                            书写代码：
                                super（参数1，参数2）
                            工作原理：
                                def super（cls，inst）：
                                    mro = inst.__class__.mro()
                                    return mro[mro.index(cls)+1]
                        常用具体语法形式
                            super()
                        注意：
                            不能用类调用和super共同使用作为资源的累加

"""


# ---------------------------------------类的特性（继承）------------------------------------
# import inspect
#
#
# class Animal:
#     # 资源：属性和方法
#     # 设置不同权限的属性和方法 ，看在子类当中能否访问到这些资源
#     a = 1
#     _b = 2
#     __c = 3
#
#     def t1(self):
#         print('t1')
#
#     def _t2(self):
#         print('t2')
#
#     def __t3(self):
#         print('t3')
#
#     def __init__(self):
#         print('init,animal')
#     pass
#
#
# class xxx:
#     pass
#
#
# # 单继承
# class Dog(Animal):
#     def test(self):
#         print(self.a)
#         print(self._b)
#
#         self.t1()
#         self._t2()
#         self.__init__()
#     pass
#
#
# # # 多继承
# # class Dog1(Animal, xxx):
# #     pass
#
# d = Dog()
# d.test()
#
# # 查看类的继承问题
# print(inspect.getmro(Dog))


# ---------------------------------------类的特性（继承-资源的覆盖）------------------------------------
# class D:
#     age = 'd'
#     pass
#
#
# class B(D):
#     age = 'b'
#     pass
#
#
# class C(D):
#     age = 'c'
#
#     def test1(self):
#         print('c')
#     pass
#
#
# class A(B, C):
#     pass
#
#
# print(A.mro())
# a = A()
# print(a.age)
# print(a.test1())


# ---------------------------------------类的特性（继承-资源的累加）------------------------------------
#
# class B:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#
#     def t1(self):
#         print('t1')
#
#     @classmethod
#     def t2(cls):
#         print('t2')
#
#     @staticmethod
#     def t3():
#         print('t3')
#
#
# class A(B):
#
#     def __init__(self):
#         self.e = 2
#     pass
#
#
# a1 = A()
# print(a1.b)
# a1.b = 3
# print(a1.__dict__)
# print(A.__dict__)
# print(A.a)
# print(a1.t1())
# print(A.t2())


# ---------------------------------------类的特性（继承-资源的累加-通过类名.__init__方法加入资源）------------------------------------

#
# class D:
#     def __init__(self):
#         print('d')
#
#
# class C(D):
#     def __init__(self):
#         D.__init__(self)
#         print('c')
#
# class B(D):
#     def __init__(self):
#         D.__init__(self)
#         print('b')
#
#
# class A(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print('a')
#
#
# a = A()
# # 总结：出现重复调用


# ---------------------------------------类的特性（继承-资源的累加-通过super(参数1，参数2）------------------------------------

#
# class B:
#
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#
#     def t1(self):
#         print('t1')
#
#     @classmethod
#     def t2(cls):
#         print('t2')
#
#     @staticmethod
#     def t3():
#         print('t3')
#
#
# class A(B):
#
#     def __init__(self):
#         # super(A, self).__init__()# python2.2之后的版本
#         super().__init__()
#         self.e = 2
#
#     def tt1(self):
#         print('t1')
#
#     @classmethod
#     def tt2(cls):
#         super().t2()
#         print('t2')
#
#     @staticmethod
#     def tt3():
#         print('t3')
#
#
# a1 = A()
# a1.tt2()
# print(a1.__dict__)

# ---------------------------------------类的特性（继承-资源的累加-通过super(参数1，参数2）-关于菱形继承------------------------------------


class D:
    def __init__(self):
        print('d')


class C(D):
    def __init__(self):
        super().__init__()
        print('c')


class B(D):
    def __init__(self):
        super().__init__()
        print('b')


class A(B, C):
    def __init__(self):
        super(A, self).__init__()
        print('a')


a = A()
print(a.__dict__)
print(A.__dict__)
print(A.__mro__)
