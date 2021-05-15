"""
公共操作：序列所能够共同运用的操作
    运算符
    公共方法
    容器类型转换
运算符
    + 合并 支持字符串列表元组不支持字典
    * 复制 支持字符串列表元组不支持字典
    in 元素是否存在 支持字符串列表元组字典
    not in 元素是否存在 支持字符串列表元组字典
函数
    len() 计算容器总元素的个数
    del/del() 删除
    max() 返回容器中元素最大的值
    min() 返回容器中元素最小的值
    range(star，end，step) 生成从star 到 end 的数字，步长为step，供for循环使用 end的最后一个位置不包含
    enumerate(可遍历对象，start=0) 函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，
    一般用在for循环当中 start参数用来设置遍历数据的下标位置的起始值
容器类型的转换
    tuple() 将序列转换为元组
    list() 将序列转化为列表
    set() 将序列转化为集合
"""
str1 = 'aabcd'
str2 = 'bb'
list1 = [1, 2]
list2 = [10, 20]
t1 = (1, 2)
t2 = (10, 20)
dict1 = {'name': 'python', 'gender': '男'}
dict2 = {'age': '30'}
# 测试+ 运算
# 字符串
str3 = str1 + str2
print(str3)
# 列表
list3 = ['a', 'b', 'c', 'd', 'e']
# 元组
t3 = t1 + t2
print(t3)
# 测试*运算
# 字符串
str4 = str1 * 2
print(str4)
# 列表
print(list1 * 2)
# 元组
print(t1 * 2)
# 任意字符
print('-' * 10)
# 测试in与not in
# 测试字符串
print('a' in str1)
# 测试列表
print(1 in list1)
# 测试元组
print(1 in t1)
# 测试字典
print('name' in dict1)
print('python' in dict1)
print('python' in dict1.values())
# 测试len()
print(len(str1))
print(len(list1))
print(len(t1))
print(len(dict1))
# 测试max
print(max(str1))
print(max(list1))
print(max(t1))
print(max(dict1))
# 测试del
del (list1[0])
print(list1)
del (dict1['name'])
print(dict1)
# 测试range
for i in range(1, 10):
    print(i)
# 测试enumerate
for i in enumerate(list3):
    print(i)
for i in enumerate(t1):
    print(i)
for index, char in enumerate(list3):
    print(f'索引是{index}，索引值是{char}')
# 容器类型的转换
s1 = {10, 20, 30, 40, 50}
# tuple()
t4 = tuple(list1)
print(t4)
print(t1)
# list()
list4 = list(t1)
print(list4)
# set()
print(set(list3))

test_dict = {'name1': '张三', 'age1': 18}
test_dict1 = {'name': '李四', 'age': 20}
test_dict.update(test_dict1)
print(test_dict)
for every in enumerate(test_dict):
    print(every, test_dict[every[1]])
