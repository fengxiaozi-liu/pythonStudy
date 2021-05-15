"""
字典的学习目标
    字典的应用场景
    创建字典的语法
    字典的常见操作
    字典的循环遍历
字典的应用场景
    字典以一种键值对的形式出现 字典不支持下标 后期无论数据如何变化，只需要按照对应的建的名字查找就好
字典的特点
    符号是大括号
    数据为键值对出现
    各个键值对之间用逗号隔开
创建字典
    创建有数据的字典
        字典名 = {键值数据：键值key}
    创建空字典
        字典名 = {}
        字典名 = dict()
字典的新增数据操作
    字典名[key] = 数据 如果key存在则改变值，如果键值不存在则新增这个数据
字典删除数据的操作
    del()/del 删除字典或者删除指定字典的键值对 删除指定的键值对 键值对存在则删除不存在则报错
    字典名.clear() 清空字典
字典修改数据的操作
    字典序列[key] = 值
字典数据的查找
    key值查找  字典名[key]  如果key存在则返回相应的值，如果不存在则报错
    字典序列.get(key,默认值) 如果key不存在则返回第二个参数(默认值),如果省略第二个参数则返回None
    字典序列.keys() 查找字典中的key可迭代的对象 可用for循环
    字典名.values() 查找字典中所有所对应的数据是一个可迭代的对象
    字典名.items() 返回字典中的所有键值对 每一个键值对以元组的形式出现 是一个可迭代的对象
字典的循环遍历
    遍历字典中的key
    遍历字典中的value
    遍历字典中的元素
    遍历字典中的键值对 就是将key 和 value 数据分开 拆包动作需要两个临时变量
"""
# 创建有数据的字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name'])
# 创建空字典
dict2 = {}
print(type(dict2))
dict3 = dict()
print(type(dict3))
# 字典新增数据
dict1['汤小涵'] = '我老婆'
dict1['name'] = 'my'
dict1['gender'] = '女'
print(dict1)
print(dict1['汤小涵'])
# 删除字典
del dict1['name']
print(dict1)
# 新增键值对
dict1['name'] = 'my'
print(dict1)
# 字典的查找
print(dict1['name'])
# get（）方法的测试
print(dict1.get('name'))
print(dict1.get('id'))
# keys()查找字典的所有key,是一个可迭代的对象
print(dict1.keys())
# values() 查找字典所有的值,是一个可迭代的对象
print(dict1.values())
# items() 查找所有的数据 数据以键值对形式出现，每一个键值对以元组的方式存储
print(dict1.items())
# 遍历字典中的key
for key in dict1.keys():
    print(key)
# 遍历字典中的value
for value in dict1.values():
    print(value)
# 遍历字典的元素
for item in dict1.items():
    print(item)
# 遍历字典中的键值对
for key, value in dict1.items():
    print(f'{key} = {value}')
