一般文件的读取
	打开文件
	1. file = open('文件名'，'r/w/a/w+/r+/rb/rw',encoding='utf8')
		以不同的方式打开一个文件
		r 以只读的方式打开
		w 以写入的方式打开，新的内容会覆盖旧的内容
		a 以追加的方式打开，文件不存在创建文件，文件存在则追加
		w+/r+ 以可读写的方式打开
		rb	 以二进制只读的方式打开一个文件
		rw 	 以二进制写入的方式打开一个文件
	2.读取文件
		file.read()读取当前文件的内容
		file.read(n)指定读取的长度 当读取指定长度的数据时，
					读取的光标会停留在上一次读取的位置，保证数据完整性
		file.readline() 只读取一行的数据
		file.readlines() 读取所有行的数据并保存在一个列表中
	3.文件的写入
		file.write(内容.encode('utf8'))
	4.文件的关闭
		file.close()
csv文件的读写
	csv文件相当于一张excel，他的读取和写入都要借助读取或者写入对象
	打开csv文件
		file = open('文件名'，'r/w' ,encoding=utf8)
	创建一个读取或者写入对象
		r = reader(file)
		w = writer(file), w.writerow([列表])

json
	序列化：就是将内存持久化到硬盘的功能
	反序列化：将数据从硬盘加载到内存的过程
	json实现序列化
		json.dumps(数据) 将数据转化成json字符串
		json.dump(数据，open('文件名'，'w', encoding=utf8)) 
			将数据转化为json字符串并保存在指定的文件中
	json实现反序列化
		json.loads(json字符串) 将json字符串转换成python中可用的数据
		json.load(open(文件名,'r', encodingutf8))
			将文件中的json字符串转换成python中可用的数据

pickle
	pickle实现序列化
		pickle.dumps(数据) 将数据转化成二进制
		pickle.dump(数据，open(文件名,'wb')) 将数据转化成二进制写入指定的文件
	pickle实现反序列化
		pickle.loads(二进制数据) 将二进制数据转化成可以被python识别的数据
		pickle.load(open(文件名,'rb')) 以二进制的方式打开文件，并加载成python数据

异常处理：
	采用try...except...else 语句
	try：
		z = x/y
	except Exception as e:
		print('y不能做除数')
	else:
		return z
	采用raise关键字抛出一个异常
		raise valueError('输入的值错误')

with关键字
	with可以帮我们自动的关闭一个文件或者程序
	因为with有两个必要的方法__enter__ 和 __exit__
	with open(文件名,'r', encoding=utf8) as file:
		file.read()
finally关键字
	finally关键字的意思是怎么都会执行这个代码
	def chu(a,b):
		try:
		    x = a/b
		except Exception as e:
			print('不能是0')
		else:
			return x
		finally:
			print('good')
			return good
	在执行完函数之后，就会执行finally关键字，如果finally关键字里面有return
	那么他会把原来的返回值覆盖掉

正则表达式
    正则表达式是用来对字符串进行检索和替换
    正则表达式的使用需要使用re模块
    import re
    正则表达式中的方法
    	re.match(正则规则，字符串)  返回re.Match类对象
    	re.serch(正则规则，字符串)	返回re.Match类对象
    	re.fullmatch(正则规则，字符串) 返回re.Match类对象
    	re.finditer(正则规则，字符串)	 返回一个迭代器，迭代器中的每一个数据都是一个re.Match类对象
    	re.findall(正则规则，字符串)  返回一个匹配到所有结果的列表
    re.Match类对象中的方法
    	groups
	    	对象名.groups() 默认拿到第0组的数据
	    	对象名.groups(1,2) 拿到第1组和第2组的数据
	    	对象名.groups(分组名) 拿到指定的分组
	    groupdict
	    	对象名.groupdict() 将分组名和数据一一对应放到一个字典中

	正则规则
		\n 表示换行
		\t 表示制表符
		\d 表示[0-9]的任意一个数字
		\w 表示数字字母或者是下划线
		\s 表示非空字符，空字符包括空格,制表或者换行
		| 表示或者 
		[x-y] 表示选取x-y的任意一个数
		{n,} 表示n次及以上次数
		{,m} 表示m次以下
		{n,m} 表示n次以上m次以下的次数
		. 表示任意字符
		* 表示任意次数
		+ 表示一次及以上次数
		？ 表示一次及以下
		^ 表示必须以什么开头
		$ 表示必须以什么结尾
		() 表示一个分组
		？P<name> 表示给这个分组命名
	正则修饰符
		re.S 忽略换行符
		re.I 表示忽略大小写
		re.M 表示可以多行匹配

	正则替换 
		re.sub(正则规则，要替换的字符串或者是一个函数，字符串)

	贪婪模式和非贪婪模式
		贪婪模式就是尽可能多的匹配
		非贪婪模式就是尽可能少的匹配
	re.compile()方法
		r = re.complie(正则规则) 生成一个匹配对象
		x = r.search(字符串)

