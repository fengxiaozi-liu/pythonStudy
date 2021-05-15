"""列表是一次性处理多个数据，可用于增删改查
查找数据使用的函数：
    index(数据，开始下标位置，结束下标位置) 返回指定位置的下标
    count(数据) 统计指定数据在当前列表出现的次数
    len(列表名) 返回列表的长度
判断数据是否存在
    in 如果数据在列表里面返回True，否则返回False
    not in 与 in相反
    作用：可用于判断邮箱是否存在
    属于一个公共的操作
增加数据的函数
    列表序列.append(数据) 列表结尾增加数据，如果是一个序列，则增加增加整体的列表序列
    列表序列.extend(数据) 列表结尾增加数据可以增加序列,如果追加的是一个序列，则将序列拆开一个一个的追加
    列表序列.insert(位置下标，数据)在指定的位置追加数据
列表的删除操作
    del 列表名 删除列表
    del 列表名[下标] 指定位置做删除
    列表名.pop(下标） 删除指定位置的数据 并且返回该数据 如果不写下标指定最后一个数据
    列表名.remove(数据) 移除列表中的某个数据的第一个匹配项 如果该数据重复
    列表名.clear() 清空列表
修改操作
    列表名[下标]修改指定下标的数据
    列表名.reverse() 逆置函数
    列表名.sort(key=None,reverse=False) 排序reverse默认为false升序排列
    补充：sort的另一种用法
        语法：
            列表名.sort（key=函数（参数））
            需知：
                其中key=函数（参数）是排列列表中字典的用法
                sort会按照key的规则自动的遍历列表中的元素，其中key是一个带有一个参数的函数
列表的复制
    列表名.copy() 复制列表
    为什么复制列表的数据：防止文件数据丢失
列表的循环遍历 按需求依次访问列表中的数据
    while循环实现遍历
        准备表示下标的数据
        循环while循环体
    for循环遍历
        准备临时变量
        遍历序列中的数据
列表嵌套
    列表中有一个子列表
    用逗号隔开子列表
    子列表中的数据依然用逗号隔开
总结：
    常用的操作方法
"""
# 返回下标
name_list = ['Tom', 'lily', 'Rose']
print(name_list[0])
# 测试index()函数
print(name_list.index('Tom'))
# 测试count()函数
print(name_list.count('Tom'))
# 测试len()函数
print(len(name_list))
# 测试 in
print('Tom' in name_list)
# 测试not in
print('Tom' not in name_list)
"""
需求：判断用户是否存在
如果存在可以输入账号，如果不在则提示
运用的相应函数
if else
input

"""
""""
name = input('请输入你的账号')
if name in name_list:
    print(f'您输入的名字是{name},已经存在了')
else:
    print(f'您输入的名字是{name},可行')
    name_list.append(name)
print(name_list)
"""
# 测试append()函数
name_list.append('xiaoming ')
name_list.append([11, 22, 33])
print(name_list)
# 总结:列表是一个可以改变的数据
# 测试extend()
name_list.extend(['xiaoming ', 'xiaohong'])
print(name_list)
# 测试insert()函数
name_list.insert(2, '小明')
print(name_list)
# 测试del
"""
del name_list
print(name_list)
"""
# pop()函数测试
name_list.pop(2)
print(name_list)
# 测试remove()
name_list.remove('xiaoming ')
print(name_list)
# 测试修改指定下标的数据
name_list[0] = 'abc'
print(name_list)
# 测试逆序
name_list.reverse()
print(name_list)
# 测试sort
list1 = [1, 3, 2, 4, 5]
list1.sort(reverse=True)
print(list1)
# 测试copy()
list1 = name_list.copy()
print(list1)
# 测试while循环遍历列表
i = 0
while i < len(name_list):
    print(name_list[i])
    if name_list[i] == 'Rose':
        break
    i += 1
# 测试for循环
for each in name_list:
    print(each)
# 测试列表的嵌套
name_list1 = [['张三', '李四', '王五'], ['小明', '小华', '小红'], ['李磊']]
print(name_list1)
print(name_list1[0])
print(name_list1[0][1])
"""
需求：
有三个办公室，八位老师，八位老师随机分配到3个办公室
"""
import random

teacher = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
office = [[], [], []]
for each_teacher in teacher:
    j = random.randint(0, 2)
    office[j].append(each_teacher)
print(office)
i = 0
for each in office:
    print(f'办公室{i + 1}的人数是{len(each)},老师成员是 ')
    for each_name in each:
        print(each_name)
    i += 1

# 关于sort函数的补充
list1 = [
    {'name': 'zhangsan', 'age': 18, 'heiget': 180, 'score': 98},
    {'name': 'lis', 'age': 20, 'heiget': 179, 'score': 97},
    {'name': 'wangwu', 'age': 19, 'heiget': 182, 'score': 96},
    {'name': 'jack', 'age': 21, 'heiget': 185, 'score': 100}
]
list1.sort(key=lambda n: n['age'])
for each_dict in list1:
    print(each_dict)
