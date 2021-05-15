"""
打印一张九九乘法表
使用循环计数打印1-100的和
统计一百以内个位数是2并且能够被三整除的数
"""


class Count:
    def __init__(self):
        self.num = 0
        self.num1 = 1
        self.num2 = 1
        self.cache = []
        self.cache2 = set()
        self.cache3 = [1, 5, 9, 8, 2]

    # 设计一个九九乘法表的函数
    def chengfabiao(self):
        for a in range(1, 10):
            for b in range(1, a + 1):
                result1 = a * b
                print(f'{b}*{a}={result1}', end='\t')
                if a == b:
                    print()

    # 设计秋一百以内的和
    def total1(self):
        for i in range(101):
            self.num += i
        return self.num

    # 统计一个一百以为个位数是2并且能够被三整除的数
    def tongji(self):
        for i in range(100):
            if i % 10 == 2 and i % 3 == 0:
                self.cache.append(i)
        return self.cache

    # 输入任意一个正整数求它是几位数
    def weishu(self):
        a = int(input('输入你想要的正整数'))
        b = len(str(a))
        print(f'您输入的{a}，是{b}位正整数')

    # 打印所有的水仙花数
    def shuixianhua(self):
        for i in range(100, 1000):
            a = int(str(i)[0])
            b = int(str(i)[1])
            c = int(str(i)[2])
            if i == a ** 3 + b ** 3 + c ** 3:
                self.cache2.add(i)
        return self.cache2

    # 求斐波那契数列第n个数的值
    def feibonaqie(self, n):
        for i in range(n - 2):
            a = self.num1
            self.num1 = self.num2
            self.num2 = a + self.num2
        return self.num2

    # 冒泡排序
    def maopaopaixu(self):
        # 依次找到第n大的数
        for j in range(len(self.cache3)-1):
            # 找到没排序好的最大对的数方法后面
            for i in range(len(self.cache3) -1):
                if self.cache3[i] > self.cache3[i+1]:
                    self.cache3[i], self.cache3[i + 1] = self.cache3[i+1], self.cache3[i]
        return self.cache3


c = Count()
print(c.shuixianhua())
print(c.total1())
print(c.tongji())
print(c.feibonaqie(12))
print(c.maopaopaixu())
