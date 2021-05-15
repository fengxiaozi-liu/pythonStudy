"""
字符串的常用操作
    切片：截取其中一部分数据的操作
        字符串[下标] 拿到字符串的某个数据
        序列名[start:end:step] start开始位置下标 end结束位置下标 step为步长即选取间隔
        保证选取方向一致
    字符串的修改
        字符串序列.replace(旧字符串，新字符串，替换次数) 做子串的替换
        字符串序列.split(分隔符，num) 返回一个列表 做子串的分割 num为分割字符串出现的次数，即将来返回的数据为num+1
        字符或者子串.join(多字符串组合序列) 将列表中的数据用字符串合并成一个新的字符串
    字符串的查找（查找字符串出现的位置和出现的次数都叫做字符串的查找）
        字符串序列.index(子串，开始下标位置，结束下标位置） 如果存在返回下标位置若不存在会报错
        rindex() 从右侧开始查找
        字符串序列.find(子串，开始下标位置，结束下标位置)  如果存在返回开始位置的下标若不存在返回-1
        rfind() 从右侧开始查找
        字符串序列.count(子串，开始下标位置，结束下标位置) 返回子串从开始位置到结束位置出现的次数
    字符串的判断
        字符串序列.startswith(子串,开始下标位置,结束下包位置) 判断字符串是否以指定字符串开始 返回一个布尔型数据
        如果是则返回True 不是则返回False
        字符串序列.endswith(子串，开始下标位置，结束下表位置) 判断字符串是否以指定字符串结束 返回一个布尔型的数据
        如果是返回True否则返回False

    字符串中的两个强大功能：
        功能1的函数
            eval(字符串名)
                作用：可以执行字符串里的代码
        功能2的函数
            import json
            json.dumps(变量名） 变量可以是字典。列表。元组。集合等
                作用：可以将字典、列表、元组、集合等转换为字符串供其他语言进行识别
            json.loads(变量名) 这里的变量名是字符串的名字
                作用：可以将字符串里面的内容转换为Python中可以执行的语言
"""
# 字符串的切片
str1 = 'abcdefg'
print(str1[1:2:2])
# find()
print(str1.find('e', 1, 5))
# count()
print(str1.count('e'))
# replace()
print(str1.replace('e', 'new'))
# split()
print(str1.split('c'))
list1 = list()
for i in str1:
    print(i, end=' ')
    list1.append(i)
print('\n')
print(list1)
# join()
print('.....'.join(str1))
print(str1)
# startwith与endwith
print(str1.startswith('a', 0, 3))
print(str1.endswith('f', 4, 9))

wxp = 'input("请输入你想要的数字 ")'
print(eval(wxp))
