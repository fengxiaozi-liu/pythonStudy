"""
模块：
    定义：
        在Python里面的一个py文件，就可以理解为模块
    注意：不是所有的py问价都能作为一个模块被导入
         如果想要一个py文件能够被导入，模块名字必须要遵守命名规则
    语法：
        import 模块名 使用import直接导入一个模块
        能够使用模块里面的所有属性和方法

        from 模块名 import 函数名  导入一个模块里面的某一个方法或者变量
        from package import 模块 导入包里面的某一个模块

        from 模块名 import * 导入模块里面的“所有”方法和变量
        '所有'的本质是读取模块里面的__all__属性，看这个属性定义了哪些变量和函数
        如果模块里面没有定义__all__才会导入所有不以一个下划线开头的变量和函数
        __all__ 是一个列表

        from 模块名 as 别名  导入一个模块并且给它起一个别名

        from 模块名 import 函数名 as 别名  将一个模块中的函数导入并且给它起一个别名

        from package.包里面的模块 import 函数名  导入包里面其中一个模块中的其中一个函数

常见的内置模块：
    1os模块（OperationSystem）
        作用：
            用来调用操作系统里面的方法
        方法：
            os.name 获取操作系统的名字
                nt windows操作系统的名字
                posix unix操作系统的名字
            os.sep  获取路径的分割符
                \  windows系统的分隔符
                / 非windows系统的分割符
            os.path 获取路径
                os.path.abspath(文件名) 获取文件的绝对路径
                os.path.isdir(文件名) 判断是否是文件夹
                os.path.isfile(文件名)  判断是否是文件
                os.path.exists(文件名)  判断是否存在
                os.path.splitext(文件名) 获取文件名和文件的后缀
            os.getcwd() 获取当前的工作目录 即当前的脚本工作目录
            os.chdir(‘test') 改变当前脚本工作目录 ，相当于shell下的cd命令
            os.rename(’文件名‘，’文件名1‘) 文件重命名
            os.remove(’文件名‘)  删除文件
            os.rmdir ('文件夹名') 删除空文件夹
            os.removedirs('文件夹名') 删除空文件夹
            os.mkdir('文件夹名') 创建一个文件夹
            os.listdir('目录名') 列出当前目录里面的所有文件和文件夹
            os.chdir('../') 返回上一级目录
            os.environ 获取环境变量的配置
            os.environ.get('PATH') 获取指定环境的配置
    2.sys模块 系统相关的模块
        sys.exit() 退出，让程序终止和内置函数exit功能一样
        sys.path 返回一个列表 表示查找模块的路径,如果路径中有这个模块就可以使用，没有就会报错
        sys.stdin 接收用户的输入，可以像input一样接收用户的输入。 和input相关
        sys.stdout 标准输出 修改sys.stdout 可以改变默认的输出位置 读取键盘里的输入数据
            语法：
                sys.stdout = open(file_name,'w', encoding='utf8')  创建数据输出保存的文件
                print(数据） 这时候数据输出的结果就会保存到上面创建好的file_name文件中去
        sys.stderr 错误输出 修改sys.stderr可以修改错误输出的默认位置
            语法：
                sys.stderr = open(file_name,'w', encoding='utf8')  创建数据输出保存的文件
                print(数据） 这时候输出的错误数据就会保存到上面创建好的file_name文件中去
    3.math模块 数学相关的模块
        inf 无限
        math.factorial(num) 求阶乘的
        math.floor(num)  向下取整数
        math.cell(num) 向上取整
        math.pow(num1,num2) 求num1的num2次方
        round(num1,n) 四舍五入到指定的位数 是Python中的内置函数不是math模块中的
        math.sin(弧度） 算正弦函数
        math.cos(弧度） 算余弦函数
        math.tan(弧度) 算正弦函数
    4.random模块 用来生成一个随机的数
        random.randint(a,b) 用来生成a-b的随机整数
        random.random() 用来生成从0-1的浮点数包含0不包含1
        random.randrange(a,b） 生成一个[a,b)的随机整数包含a不包含b
        random.choice(可迭代对象) 用来在可迭代对象里随机的抽取一个数据
        random.sample(可迭代的对象) 在可迭代对象里面随机的抽取n个对象
    5.datetime模块
        涉及四个类 date类用来显示日期 time类用来显示时间  datetime类用来显示日期时间 timedelta类用来计算时间
        datetime.datetime.now() 获取当前的时间
        datetime.date(年份，月份，日） 创建一个日期
        datetime.time(时，分，秒) 创建一个时间
        datetime.datetime.now() + timedelta(num) 计算num天后的日期和时间
        应用场景：
            设计自动化的脚本的时候
    6.time模块 计算时间
        time.time() 获取1970-01-01 00:00:00 UFC 到现在秒数  是一个时间戳
        time.strftime(格式化) 按照指定的格式输出时间
        time.asctime() 返回当前的时间 需要的参数是一个元组
        time.ctiem(时间戳) 传入一个时间戳返回当前的时间
        time.sleep(num) 暂停num秒
    7.calendar模块 日历模块
        calendar.calendar(年份）打印指定年份的日历
        calendar.setfirstweekday(calendar.SUNDAY) # 设置每周日的起始码，周一到周日分别对应0~6
        calendar.firstweekday() 返回当前每周起始日期设置，默认情况下，首次载入calendar模块是返回0，即是星期一
        calendar.isleap(year) 判断是否是闰年
        calendar.leapdays(year1,year2) 从year1到year2有几个闰年
        calendar.month(year,month) 打印第几年第几月的日历
        应用场景：
            做后台服务的时候有可能用到
    8.hashlib模块和hmac模块  用来数据加密的
        hashlib 模块主要支持两个算法 md5 和 sha 加密
        加密方式：
            单项加密
                定义：
                    只有加密的过程没有解密
                相关算法：
                    md5算法
                    x = hashlib.md5() 生成md5的对象
                    x.update('abc'.encode('utf8')) 进行加密
                    print(x.hexdigest()) 拿到一个十六进制的数
                    注意：需要加密的属性必须转换成二进制编码
                        'abc' ==> 十六进制数的一个地址 只有从明文到密文的过程，不能返回回来
                    其他：
                        文件的md5
                    sha算法
                    y = hashlib.sha1('加密对象'.encode())   用sha1进行加密
                    y = hashlib.sha224('加密对象'.encode())  用sha224进行加密 224指的是位数
                    y = hashlib.sha256('加密对象'.encode())  用sha256进行加密
                    y = hashlib.sha384('加密对象'.encode())  用sha384进行加密
                    print(y.hexdigest()) 拿到一个十六进制的地址数
                    补充：一个十六进制占4位 一个字节占8位
            hmac加密：
                hmac加密可以指定秘钥
                z = hmac.new('h'.encode(),'加密对象‘.encode(),加密的算法) 用h对你好进行加密 h是秘钥  加密的算法可以指定
            对称加密
            非对称加密
                rsa算法
    9.copy模块 拷贝模块
        对象1名= copy.copy(对象2名)  拷贝对象2 浅拷贝
        对象1名 = copy.deepcopy(d对象2名) 拷贝对象2 深拷贝
    10.uuid模块 用来生成全局唯一一个id的模块
        作用： 生成一个32个数，每一个有十六个选择 一共有16**32个选择
        应用：
            保证整个系统里面是唯一的一个
        相关函数：
        uuid.uuid1() 基于MAC地址，时间戳，随机数生成唯一的uuid，可以保证全球范围内的唯一性
        uuid.uuid2() 与uuid1相同，不同的是把时间戳的前4位置换成posix的UID，Python中没有DEC算法，因此Python中没有这个方法
        uuid.uuid3(namespace,name)
            通过计算一个命名空间和名字的md5散列值给出一个uuid，所以可以保证命名空间的不同名字具有不同的uuid，但是相同名字就有
            相同的uuid。namespace并不是一个自己手动指定的字符串或者其他量，而是uuid模块中本身的一些值，这些值本身也是uuid对象
            根据一定的规则计算出来的
            这些值举例：uuid.NAMESPACE_DNS uuid.NAMESPACE_OID
        uuid.uuid4() 通过伪随机数得到uuid是有概率重复的
        uuid.uuid5(namespace,name) 和uuid3()作用相同只是采用的是sha1算法
        注意：
            uuid3和uuid5是使用传入的字符串根据指定算法算出来的，是固定的
            开发中最常用的uuid4
        应用场景：
            给多个人发信息的时候添加一个uuid


"""

# ----------------------------------------------关于os模块-------------------------------
# os.name
import os

print(os.name)
# os.sep
# ----------------------------------------------关于sys模块-------------------------------
import sys

print(sys.path)
print('-' * 30)
# ----------------------------------------------关于datatime模块-------------------------------
import datetime as dt

# 获取当前时间
print(dt.datetime.now())
# 创建一个日期
print(dt.date(2020, 8, 15))
# 创建一个时间
print(dt.time(20, 15, 50))
# 获取三天后的时间
print(dt.datetime.now() + dt.timedelta(3))
print('-' * 30)
# ----------------------------------------------关于time模块-------------------------------
import time

# 获取时间戳
print(time.time())
# 格式化输出时间
print(time.strftime('2020-8-15'))
print(time.ctime(1597494596))
print('-' * 30)
# ----------------------------------------------关于calendar模块-------------------------------
import calendar

# 打印2020年的日历
print(calendar.calendar(2020))
# 设置每周的起始码
calendar.setfirstweekday(calendar.SATURDAY)
print(calendar.calendar(2020))
# 返回当前每周起始日期
print(calendar.firstweekday())
# 判断是否是闰年
print(calendar.isleap(2020))
# 计算从2000到2020年有几个闰年
print(calendar.leapdays(2000, 2020))
# 打印2020年3月份的日历
print(calendar.month(2020, 3))
print('-' * 30)
# ----------------------------------------------关于hashlib模块-------------------------------
import hashlib

# 用md5进行加密
x = hashlib.md5()
x.update('abc'.encode('utf8'))
print(x.hexdigest())
# 用sha进行加密
# 用sha1进行加密
h1 = hashlib.sha1('1'.encode('utf8'))
print(h1.hexdigest())
# 用sha224进行加密
h2 = hashlib.sha224('1'.encode('utf8'))
print(h2.hexdigest())
# 用sha256进行加密
h3 = hashlib.sha256('1'.encode('utf8'))
print(h3.hexdigest())
# 用sha384进行加密
h4 = hashlib.sha384('1'.encode('utf8'))
print(h3.hexdigest())
import hmac

h = hmac.new('h'.encode(), '您好'.encode(), hashlib.sha224)
print(h.hexdigest())
print('-' * 30)
# ----------------------------------------------关于uuid模块-------------------------------
import uuid

# 生成一个随机的uuid
print(uuid.uuid1())
print(uuid.uuid4())
# 生成固定的uuid
print(uuid.uuid3(uuid.NAMESPACE_DNS, '张三'))
print(uuid.uuid5(uuid.NAMESPACE_DNS, '张三'))
print('-' * 30)

# ----------------------------------------------关于sys(stdin stdout stdeer)模块-------------------------------

