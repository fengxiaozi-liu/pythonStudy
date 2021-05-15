"""
序列化：
    将数据从内存持久化保存到硬盘的过程
    file_name = open('文件路径', 'w', encoding='uft8/gbk')
    1.file_name.write(数据)
        write只能写入字符串或者二进制
        列表字典和数字都不能直接写入到文件里
    2.解决只能写入字符串的缺点
        思想：
            将数据转换成字符串或者二进制写入
        解决方案：
            1.repr(数据变量名)/str(数据变量名)
            2.使用json模块转换成字符
                json.dumps(数据)
                    dumps的作用是将数据转换成json字符串 不会讲数据保存到文件里
                json.dump(数据，文件名)
                    dump作用是直接将数据转换成json字符串并将数据写入到指定文件
            3.使用pickle模块转转成二进制
                1.dumps：是将数据转换成pickle二进制 不会讲数据保存到文件里
                    file_name = open('文件名', 'wb') 以二进制方式写入
                    变量名 = pickle.dumps(数据变量名)
                    file_name.write(变量名）
                2.dump： 将数据转换pickle二进制并写入到文件中去
                    file_name = open('文件名', 'wb')
                    pickle.dump(数据变量名,file_name)
反序列化：
    将数据从硬盘加载到内存的过程
    1.json反序列化方法
        1.loads： 将json字符串加载成为Python里的数据 json中的loads需要的是一个字符串的参数
           接收数据变量名 = json.loads(json字符串中的数据）
        2.load：读取文件，把读取json字符串的内容加载成Python里的数据  json中load接收的是一个文件
           接收数据变量名 = json.load(file_name:要读取的文件名)
    2.pickle反序列的方法
        1.loads 将pickle二进制数据加载成Python里面的数据  pickle中的loads需要的是一个二进制数据类型的参数
            接收数据变量名 = pickle.loads(file_name.read()）
        2.load 读取文件并把读取的pickle二进制内容加载成Python里面的数据 pickle中的load需要的仍然是一个文件
            接收数据变量名 = pickle.load(file_name:要读取的文件名)

补充：
    Python的类型在完成json转换后，其类型在json中存储
    Python              json
    dict                object
    list，tuple         array
    str                 string
    int，float          number
    True                ture
    False               false
    None                null
json和pickle的应用场景：
    pickle用来将数据原封不动转换成为二进制，但是这个二进制只能在Python中识别。但是不能够夸平台使用
    json中只能保存一部分信息，作用是用来在不同平台之间的传递数据是，json中存储的都是基本的数据类型

"""

# write只能写入字符串或者二进制
# 列表字典和数字都不能直接写入到文件里

# 1.解决方案是将数据转换成repr/str   使用json转换 json的本质就是字符串，区别在于就送里要用双引号表示字符串
# 2.将数据转换成二进制 使用pickle模块
import json, pickle

file = open('name.txt', 'w', encoding='utf8')
name = ["zhangsan", "lisi", 18]
# json中dumps的作用是将数据转换成字符串
# x = json.dumps(name)
# json中dump直接将数据转换成json字符串并将数据写入到指定文件
# file.write(x)
json.dump(name, file)
file.close()
# json中loads 的使用将字符串转换为原来的类型
x = '{"name":"zhangsan", "age":18}'
p = json.loads(x)
print(p)
print(p['name'])
# json中load的使用
file1 = open('name.txt', 'r', encoding='utf8')
y = json.load(file1)
print(y)
print(y[0])
file1.close()

# pickle模块序列化
# 使用pickle中的dumps来序列化数据
file2 = open('name2.txt', 'wb')
name1 = {'姓名': '张三', '年龄': 18, '身高': 180, '体重': 56}
pk1 = pickle.dumps(name1)
file2.write(pk1)
file2.close()
# 使用pickle中的dump来序列化数据
file3 = open('name3.txt', 'wb')
pickle.dump(name1, file3)
file3.close()
# 使用loads读取到使用pickle二进制话的数据并将它写入Python中来
file4 = open('name3.txt', 'rb')
pickle.loads(file4.read())
file4.close()
# 使用load读取到使用pickle中二进制的数据并写入到Python中来
file5 = open('name3.txt', 'rb')
y = pickle.load(file5)
print(y)
file5.close()


# 用pickle存储对象
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def run(self):
        print('狗会跑')


d_dict = []
d = Dog('大黄', '白色')
d1 = Dog('黑色', '黑')
d_dict.append(d)
d_dict.append(d1)
# 将狗d对象存储到dog.txt文件中去
pickle.dump(d_dict, open('dog.txt',  'wb'))

# 将写入的对象读取出来
d2 = pickle.load(open('dog.txt', 'rb'))
print(d2[0].name, d2[0].color)
print(d2[1].name, d2[1].color)


# # 用json字符串存储对象
# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(f'{self.name}正在吃饭')
#
#
# p = Person('李四', 20)
# json.dump(p.__dict__, open('json存储对象.txt', 'w', encoding='utf8'))
#
# p1 = json.load(open('json存储对象.txt'))
#
# print(p1)
