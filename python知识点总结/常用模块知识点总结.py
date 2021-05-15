pip模块
	pip install 包名 -i url 从指定的地址下载指定的包
		url 常用的有 https：//mirrors.aliyun.com/pypi/simpple
					https：//mirrors.clound.tencent.com/pypi/simpple
	pip uninstall 包名

	pip list/pip freeze 用来列出当前环境安装的模块名和版本号

	pip freeze > requirment.txt 把安装的模块名和版本号输入到一个文件中操作

	pip install -r requirment.txt 从指定的文件中下载模块名和版本号

os模块
	操作系统模块，用来调用操作系统里面的方法
	os.name 用来获取操作系统的名字
	os.sep 获取路径的分割符
	os.path 获取路径
		os.path.abspath 获取文件的绝对路径
		os.path.isdir 判断是否是文件夹
		os.path.file 判断是否是一个文件
		os.path.exsits 判断文件是否存在
		os.paht.splitext 获取文件的文件名和文件后缀
	os.remove() 删除指定文件
	os.rename() 为文件重命名

sys模块
	系统相关的模块
	sys.exit() 退出
	sys.path 返回一个列表，表示查找模块的路径，在列表中存在的就可以使用
	sys.stdin 标准化输入和input相似
	sys.stdout(open(文件名,w,encoding=utf8)) 把信息标准化输出到指定的文件
	sys.stderr(open(文件名,w,encoding=utf8)) 把错误的信息标准化输出到一指定的文件

random模块
	生成随机数相关的模块
	random.randint(0,2) 在0-2之间生成一个随机的整数
	random.randrang(0,2) 在0-2之间生成一个随机的整数，但是不包括2
	random.random() 生成一个0-1的随机数
	random.choic(迭代器) 从迭代器中随机的抽取一个数据
	random.sample(迭代器) 从迭代器中随机的抽取n个对象

datatime模块
	datetime.datetime().now() 获取当前的时间
	datetime.date(2000,5,23) 生成一个2000-5-23的日期
	datetime.time(12,24,50) 生成一个12:24:50的时间
	datetime.datetime().now() + timedelta(day=3) 生成一个三天后的时间

time模块
	time.time() 生成一个时间戳
	time.ctime(时间戳) 根据时间戳生成一个时间
	time.sleep(n) 让程序停止n秒后运行
calendar模块
	日历模块
	calendar.calendar(xx) 打印第x年的日历

hashlib模块
	加密模块
	hashlib.md5() 生成一个md5的对象用md5进行加密
		hashlib.md5().update('abc'.encode('utf8'))	对abc进行md5加密

	hashlib.sha1()/hashlib.sha224()/hashlib.sha256() 用sha进行加密
		hashlib.sha224('abc'.encode('utf8')) 对abc进行sha224加密

hmac模块
	加密模块
	hmac('h'.encode('utf8'）, '你好'.encode('utf8')， hashlib.sha224)
		采用hashlib.sha224对你好进行加密，其中h是秘钥
		

	
