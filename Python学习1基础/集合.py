"""
集合的学习目标
    集合的创建
    集合的数据特点
    集合的常见操作
创建集合
    集合中的数据是没有重复的 集合没有顺序不支持下标的操作
    {}创建集合可以使用大括号 但是不能创建空集合
    set() 创建集合可以使用set() 并且空集合的创建只能使用set()
集合增加数据
    集合名.add(数据) 可用于追加一个单一的数据 增加数据如果集合中已经存在该数据，则不进行改变 可追加到任意一个位置
    集合名.update(数据)  可用于追加序列
集合删除数据
    集合名.remove(数据) 删除集合中的指定数据，数据不存在则报错
    集合名.pop() 随机删除某个数据，并且返回这个数据
    集合名.discard() 删除集合中的指定数据 如果数据不存在也不会报错
集合查找数据
    in 判断数据在集合里面
    not in 判断数据不再集合里面

"""
# 创建有数据的集合
s1 = {10,20,30,40,50}
s2 = {10,30,20,10,40,30,50}
print(s1)
print(s2)
s3 = set('abcdefg')
print(s3)
# 创建空集合
s4 = set()
print(type(s4))
# 测试集合增加数据add() 集合是一个可变数据
s1.add(100)
print(s1)
# 测试update()
s1.update([10,20,60,70,90])
print(s1)
# 测试remove()
s1.remove(10)
print(s1)
# 测试discard()
s1.discard(10)
print(s1)
# 测试pop()
del_num = s1.pop()
print(s1)
print(del_num)
# 测试 in 与not in
print(10 in s1)
print(10 not in s1)
