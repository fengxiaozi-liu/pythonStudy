"""
python的生命周期
    概念：指的是一个对象从诞生到消亡的过程
    涉及问题：
        如何监听一个对象的生命过程
        Python是如何掌控一个对象的生命
    监听对象的生命周期
        __new__方法:
            当我们创建一个对象的时候给这个对象分配内存的方法
            通过拦截这个方法，可以修改对象的创建过程
        __init方法
            当一个对象创建出来的时候增加一个附加的信息
        __del__ 方法
    内存管理机制
        存储方面：
            1Python中万物皆对象
                不存在基本数据类型
            2所有对象都会在内存中开辟一块空间
                会根据不同的类型和内容开辟不同的空间
                返回该空间的地址给外界（接收），用于后续的操作
                    可以通过id（）函数获取内存地址（十进制）
                    可以通过hex()函数获取内存地址（十六进制）
            3对于整数和短小的字符，Python会进行缓存，不会创建对个相同的对象
            4容量对象，存储的其他对象，仅仅是对其他对象的引用，并不是对象本身
        垃圾回收方面
            引用计数器 getrefcount()函数
                概念：对象被引用计算某一对象被引用的次数
                +1场景：对象被创建 p =Person()
                       对象被引用 p2 =p1
                       对象被作为参数传到一个函数中
                       对象作为一个元素，存储在容器中 l = [p]
                -1场景：对象的别名被显示销毁 del p
                       对象的别名被赋予新的对象 p1 = 123
                       一个对象离开了他的作用域
                            一个函数执行完毕内部的局部变量关联的对象，它的引用会释放
                        对象所在的容器被销毁，或者从容器中删除对象
                查看引用计数器
                    import sys
                    sys.getrefcount() 函数
            垃圾回收
                作用
                    从经过引用计数器几次仍未被释放的对象中，找到‘循环引用’，并干掉相关的对象
                    底层机制
                        怎样找到循环引用
                            容器对象：可以引用其他对象的对象
                            1收集所用的容器，通过一个双向链表进行引用
                            2针对每一个容器对象，通过一个变量gc_refs来记录当前对应的引用计数
                            3对于每一个容器对象，找到他引用的容器对象，并将这个容器对象的引用计数-1
                            4经过步骤3之后，如果一个容器对象的引用计数为0，就表示这玩意可以被回收了，肯定是‘循环引用’
                        如何提升‘循环引用’的性能
                            分代回收
                                机制：
                                    1默认一个对象被创建出来后属于0代
                                    2经历过这一代的‘垃圾回收’后，依然存活，则划分到下一代
                                    3‘垃圾回收’的周期顺序为 0代‘垃圾回收’一定次数会触发0代和1代回收
                                                        1代‘垃圾回收’一定次数之后，触发0代，1代 和 2代回收
                                查看相关的参数
                                    import gc
                                    print(gc.get_threshold)
                                    gc.set_threshold(700,10,5)
                            垃圾回收器中，新增的个数-消亡的个数，垃圾检测达到一定的阈值之后才会触发
                    垃圾回收时机
                        自动回收
                            满足条件：
                                1垃圾回收的机制
                                    gc.enable() 开启垃圾回收机制（一般是默认开启）
                                    gc.disable() 关闭垃圾回收机制
                                    gc.isenable() 判断是否开启垃圾回收机制
                                2达到垃圾回收的阈值
                        手动回收
                            gc.collect() 回收循环引用的垃圾
            特殊场景
                循环引用
        测量对象的引用个数
"""

# -----------------------------------------监听器的方法-----------------------------------------------
# class Person:
#
#     # def __new__(cls, *args, **kwargs):
#     #     print('新建的一个对象被我拦截了')
#
#     def __init__(self):
#         self.name = 'sz'
#
#     def __del__(self):
#         print('这个对象被释放')
#
#
# p = Person()
# print(p)
# print(p.name)
# del p


# -----------------------------------------监听生命周期的小案例-----------------------------------------------
# Person ,打印一下，当前这个时刻，由Person类产生的对象，有多少个
# 创建一个实例，count + 1，删除一个实例 count - 1

# count = 0

#
# class Person:
#     count = 0
#
#     def __init__(self):
#         # global count
#         Person.count += 1
#
#     def __del__(self):
#         global count
#         self.__class__.count -= 1
#
#     @staticmethod # 或者是classmethod
#     def log():
#         print(f'当前的个数为{Person.count}')
#
#
# p = Person()
# p1 = Person()
# Person.log()
# del p
# Person.log()

# -----------------------------------------内存管理机制（存储方面）-----------------------------------------------
# class Person:
#     pass
#
#
# # 测试对象开辟的空间
# p = Person()
# print(id(p))
# print(hex(id(p)))
# # 测试整数和短小字符不会改变的空间
# num1 = 1
# num2 = 2
# print(id(num1))
# print(id(num2))
# print('-'*30)


# -----------------------------------------内存管理机制（引用计数器）-----------------------------------------------
# import sys
#
#
# class Person:
#
#    pass
#
#
# p1 = Person()
# print(sys.getrefcount(p1)-1)
# p2 = p1
# print(sys.getrefcount(p1)-1)
# del p2
# print(sys.getrefcount(p1)-1)


# -----------------------------------------内存管理机制（引用计数器 特殊场景 循环引用）-----------------------------------------------
# 内存管理机制 = 引用计数器机制 + 垃圾回收机制
# objgraph
# objgraph.count() 可以查看，垃圾回收器，跟踪的对象个数
import objgraph

#
# class Person:
#     pass
#
#
# class Dog:
#     pass
#
#
# p = Person()
# d = Dog()
# print(objgraph.count('Person'))
# p.pet = d
# d.master = p
# print(objgraph.count('Person'))
# print(objgraph.count('Dog'))
# del p, d
# print(objgraph.count('Person'))
# print(objgraph.count('Dog'))


# -----------------------------------------(垃圾回收-分代回收)-----------------------------------------------
# import gc
# # 获取垃圾回收机制的阈值
# print(gc.get_threshold())
# 设置垃圾回收机制的阈值
# gc.set_threshold(200, 5, 5)
# print(gc.get_threshold())
# -----------------------------------------(垃圾回收机制-触发时机)-----------------------------------------------
import gc
import objgraph

# 自动回收
# 垃圾回收机制的开启和关闭
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())


# 手动回收


class Person:
    pass


class Dog:
    pass


p = Person()
d = Dog()
# 创建循环引用
p.pet = d
d.master = p

del p
del d
# 调用手动触发 手动的回收
gc.collect()
print(objgraph.count('Person'))
print(objgraph.count('Dog'))
