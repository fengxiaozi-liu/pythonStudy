"""
推导式目标：更有风格的Python代码 减少代码量
    列表推导式
    字典推导式
    集合推导式
列表推导式
    作用：用一个表达式创建一个有规律的列表或控制一个有规律的列表
    列表推导式又叫列表生成式
    简单列表推导式
        列表名 = [i for i in range(start,end,step)] 创建一个从start到end以step为步长的列表
    带if的列表推导式
        列表名 = [ i for i in range(start,end) if 条件] 创建一个从start到end符合if条件的列表
    多个for循环实现列表推导式（创建元组对列表）
        列表名 = [(i,j) for i in range(start,end,step) for j in range(start,end,step)]
        创建一个以i为横坐标（i从start开始到end结束步长为step）以j为纵坐标（j从start开始到end结束以step为步长）的元组对列表
字典推导式
    作用：快速合并列表为字典或者提取字典中的目标数据
    简单字典推导式
        字典名 = {i:j for i in range()} i是key j是与i有关的算术式  for i in range（） 是相关的范围
    将两个列表合并为一个字典
        字典名 = {列表名1[下标]:列表名2[下标] for i in range(len(列表名1))}
    提取字典中的目标数据
        字典名 = {key : value for key,value in 原数据字典库 if 条件}
        按照条件从原字典中提取符合条件的key与value并且存储在一个新创建的字典中
    集合推导式
        集合名 = set(需要返回的值 for i in 列表名/元组名) 注意：集合有去重复的功能

"""
# 列表推导式
"""
需求：
    创建一个0-10的列表
    使用while循环实现
    使用for循环实现
    使用列表推导式实现
"""
list1 = []
list2 = []
i = 0
# while循环实现
while i < 11:
    list1.append(i)
    i += 1
print(list1)
# for循环实现
for i in range(0, 11):
    list2.append(i)
print(list2)
# 简单列表推导式实现
list3 = [i for i in range(1, 11, 2)]
print(list3)
# 带if的列表推导式
list4 = [i for i in range(2, 14) if i % 2 == 1]
print(list4)
# 多重for循环列表推导式
list5 = [(i, j) for i in range(0, 10) if i % 2 == 1 for j in range(1, 5) if j % 2 == 0]
print(list5)
# 简单代码实现多重for循环的列表
list6 = []
for i in range(0, 10):
    for j in range(1, 5):
        if i % 2 == 1:
            if j % 2 == 0:
                list6.append((i, j))
print(list6)
list7 = ['name', 'age', 'gender']
list8 = ['刘浩', '22', '男']
list9 = ['汤小涵', '20']
"""
需求：
  创建一个字典 key是1-5的数字 value是这个数字的2次方
"""
# 简单字典推导式
dict1 = {i: i ** 2 for i in range(1, 6)}
print(dict1)
# 将两个列表合并成字典
dict2 = {list7[i]: list8[i] for i in range(len(list8))}
dict3 = {list7[i]: list9[i] for i in range(len(list9))}
print(dict2)
print(dict3)
# 提取字典中的目标数据
counts = {'mbp': 268, 'hp': 125, 'dell': 201, 'lenovo': 199, 'acer': 99}
count1 = {key: value for key, value in counts.items() if key == 'hp'}
print(count1)
# 需求：创建一个集合，数据为下方列表的2次方
list_one = [1, 1, 2]
t1 = (1, 1, 3)
s1 = set(i ** 2 for i in list_one)
s2 = set(i + 1 for i in t1)
print(s1)
print(s2)
