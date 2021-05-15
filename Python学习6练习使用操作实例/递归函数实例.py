"""
递归函数：就是自己调用自己的函数
递归函数最重要的是找到出口（停止条件）
"""


# 求1-n的和--递归方法
def sum(n):
    # 设定一个终止循环的条件当n=0时就不在加
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


# 求1-n的和不采用递归方法
def sum1(n):
    result = 0
    # 需要借助一个for 或者 while 循环：
    for i in range(n+1):
        result += i
    return result


# 求n！-- 采用递归方法
def jiecheng(n):
    # 设定一个终止循环的条件 当n*（n-1）*（n-2）.....，当乘到2时就不再乘
    if n == 2:
        return 2
    else:
        return n*jiecheng(n-1)

def jiecheng1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# 求斐波那契数列 -- 递归方法
def feibonaqie(n):
    # 设定终止循环的条件因为是feibonaqie（n-1） + feibonaqie（n-2) 所以终止循环的条件有两个
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return feibonaqie(n-1) + feibonaqie(n-2)


# 求斐波那契数列 -- 不采用递归方法
def feibonaqie1(n):
    num1 = 1
    num2 = 1
    for i in range(0,n-2):
        a = num2
        num2 += num1
        num1 = a
    return num2


print(sum(5), end='\t')
print(sum1(5))
print(jiecheng(4),end='\t')
print(jiecheng1(4))
print(feibonaqie(5), end='\t')
print(feibonaqie1(5))
