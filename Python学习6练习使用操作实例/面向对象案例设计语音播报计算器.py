# 设计一个计算器含有基本的运算操作 以及打印相关的结果
import win32com.client


# 创建一个计算器实现简单的基本操作
class Caculator:
    # 一个接受的结果
    __result = 0

    # 创建一个判断传递的参数是否是整数的装饰器
    def __panduan(func):
        def inner(self, n):
            if not isinstance(n, int):
                raise TypeError(f'输入的{n},不是整数，重新输入')
            return func(self, n)

        return inner

    # 创建一个操作字符的装饰器
    def __Acreat_str(word):
        def __create_str(func):
            def inner(self, n):
                print(str(self.__result) + word + str(n) + '=', end='')
                return func(self, n)

            return inner

        return __create_str

    # 创建语音播报对象
    def __say(self, n):
        speaker = win32com.client.Dispatch('SAPI.Spvoice')
        speaker.Speak(n)

    # 创建语音播报对象的装饰器
    def __creat_say(word):
        def __say_words(func):
            def inner(self, n):
                self.__say(word + str(n))
                return func(self, n)

            return inner

        return __say_words

    # 创建一个展示计算结果的装饰器
    def __zsq_out(func):
        def inner(self, n):
            func(self, n)
            self.__say(f'等于{self.__result}')
            print(self.__result)
            return self

        return inner

        # 传递第一个想要加的数

    @__panduan
    @__creat_say('')
    # @__Acreat_str('')
    def __init__(self, n):
        self.__result = n

    # 加法运算
    @__panduan
    @__creat_say('加上')
    @__Acreat_str('+')
    @__zsq_out
    def jia(self, n):
        self.__result += n

    # 减法运算
    @__panduan
    @__creat_say('减去')
    @__Acreat_str('-')
    @__zsq_out
    def jian(self, n):
        self.__result -= n

    # 乘法运算
    @__panduan
    @__creat_say('乘以')
    @__Acreat_str('*')
    @__zsq_out
    def cheng(self, n):
        self.__result *= n

    # 除法运算
    @__panduan
    @__creat_say('除')
    @__Acreat_str('/')
    @__zsq_out
    def chu(self, n):
        self.__result /= n


c = Caculator(5)
c.jia(6).jian(4).cheng(5)
