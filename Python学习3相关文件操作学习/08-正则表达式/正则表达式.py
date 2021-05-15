"""
08-正则表达式
    定义：
        正则表达式是一个特殊的字符序列，计算机科学的一个概念，通常被用来检索，替换那些符合某个模式（规则） 的文本
        许多程序设计语言都支持正则表达式进行字符串的操作。在Python中需要通过正则表达式对字符串进行匹配的时候，可以使用
        re模块。re模块使Python具有全部的正则表达式功能
    作用：
        用来处理字符串，对字符串进行检索和替换
        1.查找 2.替换
    特点：
        灵活性 逻辑性 和 功能性非常强
        可以迅速地用极简单的方式达到字符串的复杂控制
    re模块中的方法
        match：
        作用：
            查找字符串，返回的一个re.Match类的对象
        具体使用：
            re.Match对象名 = re.match(r'想要的查找的字符串', ’从头开始‘)
            变量名接收的是一个re.Match类的对象
        特点：
            1.只对字符串查询一次， 返回一个re.Match类的对象
            2.match是从头开始匹配，如果字符串开始的位置与想要查找的不匹配，那么就会返回一个None
        search
        作用：
            查找字符串，返回的一个re.Match类的对象
        特点：
            1.同样只对字符串查询一次，返回一个re.Match类的对象
            2.search是从整个字符串查找如果开头没有就会往字符串的后面寻找
        具体使用：
            re.Match对象名 = re.search(r'想要的查找的字符串', ’整个字符串‘)
            变量名接收的是一个re.Match类的对象
        finditer
            作用：
                finditer 查找到所有的匹配数据放到一个可迭代对象里   返回的结果是一个可迭代的对象
                可迭代对象里的数据是匹配到的所有结果，是一个re.Match类型的对象
            具体使用：
                迭代对象变量名 = re.finditer(r'想要的查找的字符串', ’整个字符串‘)
                返回的是一个可迭代的对象，可迭代对象里面的每一个数据都是一个re.Match类型的对象
        findall
            作用：
                把查找到的所有的字符串结果放在一个列表里
            具体使用：
                变量名 = re.findall(r'想要的查找的字符串', ’整个字符串‘)
                返回的是匹配到所有结果的一个列表
        fullmatch
            作用：
               完整匹配 要查找的字符串必须完全满足正则规则才会有结果，否则是None
            具体使用：
                变量名 = re.fullmatch(r'想要的查找的字符串', ’整个字符串‘)

    re.Match类中的属性和方法：
        调用re.match re.search 或者对re.finditer进行遍历，拿到的都是re.Match类的对象
        re.Match类的属性和方法：
            pos 搜索开始查找的位置
            endpos 搜索结束查找的位置
            span() 返回匹配到结果开始位置和结束位置的下标
                注意：
                    默认是第0组

                具体使用：
                    对象名 = re.search(r'(?P<name1>正则规则)1(?P<name1>正则规则2)..(..)..', '要查找的字符串’）
                    对象名.span(num) 默认返回第0组开始和结束位置下标 如果传递一个num 则返回第num组开始的下标位置和结束的下标位置
                    对象名.span(name) 返回名字为name分组的开始下标位置和结束下标位置
            group(index = []) 某个分组匹配的结果，index可以传参，传递的参数表示第几个分组 如果index等于0，等于匹配整个正则表达式
                注意：
                    group表示正则表达式的分组
                    在正则表达式里使用一个小括号()表示一个分组
                    如果没有分组，默认只有一个组 分组从下标0开始
                    分组0表示匹配到的整个字符串
                    分组1是第一个小括号里面的字符串
                    分组2是第二个小括号里面的字符串
                    ......
                具体使用：
                    对象名 = re.search(r'(?P<name1>正则规则1)(?P<name1>正则规则2)..(..)..', '要查找的字符串’）
                    对象名.group(0) 拿到第0个分组的匹配结果
                    对象名.group(0,1,2) 拿到第0组，第1组， 第2组的匹配结果 并且保存到一个元组里面
                    对象名.group('name') 拿到名字为name的匹配结果
                    对象名.group('name1', 'name2') 拿到名字为name1，name2的匹配结果 并且保存到一个元组里面
            groups 所有分组的匹配结果，并将所有的匹配结果保存在一个元组里面，返回结果是一个含有所有匹配结果的元组
                注意：
                    是保存在元组里面
                具体使用：
                    对象名 = re.search(r'(?P<name1>正则规则1)(?P<name1>正则规则2)..(..)..', '要查找的字符串’）
                    对象名.groups()
            groupdict 返回一个字典，组名作为key 每个分组的匹配结果作为value
                注意：
                    ?P<name> 表示给分组起得一个名字
                    . 表示除了换行以为的任意字符
                    *表示任意次数
                具体使用：
                     对象名 = re.search(r'(?P<name1>正则规则1)(?P<name1>正则规则2)..(..)..', '要查找的字符串’）
                     对象名.groupdict()
            总结：
                1.上面re.Match类里面的方法都需要一个具体的对象来调用
                2.re模块中能返回对象的常用方法有re.match re.search re.finditer

        re.compile方法
            re模块里可以使用re.方法调用，还可以调用re.compile得到一个对象
            使用：
                正则对象名 = re.compile(正则规则）
                re.类对象名 = 正则对象名.search('字符串')
        正则修饰符：
            作用：
                正则修饰符是对正则表达式进行修饰的
            具体使用：
                对象名 = re.search(pattern,String, flag == 0)
                其中flag就是正则修饰符
           常用正则修饰符；
                re.S 让.匹配换行
                re.I 忽略大小写
                re.M 多行匹配影响 ^ 和 $

           补充：
            \w  表示的是字母数字和下划线_
            \d  表示的是int类型的整数
            +   表示出现一次以上
            $   表示以指定内容结尾

        正则表达式规则
            1.数字和字母都表示它本身
            2.很多字母前面添加反斜线 \ 会有特殊含义(重点)：
                \n 表示换行
                \t 表示字制表符
                \d 表示的是数字等价于[0-9]
                \D 表示的是非数字 等价于[^0-9]
                \w  表示的是字母数字和下划线_等价于[a-zA-z0-9]
                \W  表示的是标点符号与一定的运算符
                \s 任意的非打印字符
                    非字符就是空白字符包括空格 换行符 制表符
                \S 匹配非空白字符
            3.绝大多数标点符号都有特殊的含义(一般不直接使用)(重点)
                常用的标点符号
                    [] 表示一定的范围区间
                        [x-y] 表示从x-y的区间 包含x也包含y
                    | 表示或者的含义
                        x|y|z 出现的字符或者是x 或者是y 亦或者 是z
                    {} 限定前面字符出现的次数
                        {n,} 表示前面的字符出现n次以上
                        {,n} 表示前面的字符出现n次以下
                        {m,n}  表示前面的字符出现m-n次
                    . 表示任意字符
                    + 表示前面的字符出现一次以上 等价于{1,}
                    * 表示前面的字符出现0次以上 等价于{0,}
                    ? 表示前面的字符出现一次以下等价于{,1}
                    ^ 除了表示表示以指定的字符开始以外， 在[]号里还表示取反
                    $   表示以指定内容结尾

                如何使用想要表达标点符号的原有含义：
                    在标点符号的前面加上一个\  exp:\+

    正则表达式替换相关的方法
        检索的方法有 match search fullmatch finditer 都是返回一个re.Match类的对象
                   findall 返回一个列表
        替换的方法有
                   sub
        具体使用
            字符串变量名 = re.sub(r'正则规则', 要替换的字符/一个函数  要匹配的原字符)
        注意：
            函数的返回值要是一个str类型的变量


    贪婪模式和非贪婪模式
        在Python的正则规则里默认是贪婪模式
        贪婪模式
            定义：
                尽可能多的匹配
        非贪婪模式
            定义：
                尽可能少的匹配
            具体使用：
                在贪婪模式某一的字符限定了次数的后面加一个问号就变成了非贪婪模式
                re.Match对相关名 = re.search(‘正则规则部分{n}？正则规则后部分’, 要查找的字符）









"""
import re

# -----------------------------------08-正则表达式(re模块中的方法)--------------------------------------------------
# # 关于match与search
# n1 = re.match(r'hello', 'hello world good moring, hello life good afternoon')
# n3 = re.match(r'good', 'hello world good moring, hello life good afternoon')
# print(n1)
# print(n3)
# n2 = re.search(r'hello', 'hello world good moring, hello life good afternoon')
# n4 = re.search(r'good', 'hello world good moring, hello life good afternoon')
# print(n2)
# print(n4)
# print('-' * 30, '关于match与search')
#
# # 关于finditer
# n5 = re.finditer('s', 'fsadhfasndvsdhsinxcvdafjkbvasdxc')
# for i in n5:
#     print(i)
# print('-' * 30, '关于finditer')
#
# # 关于findall
# n6 = re.findall('s*\d+', 'fs5adhfas67ndvsdhs42inxcvdafjkbvas33dxc')
# print(n6)
# print('-' * 30, '关于findall')
#
# # 关于fullmatch
# n7 = re.fullmatch(r'hello', 'hello world')
# n8 = re.fullmatch(r'hello world', 'hello world')
# # h.*d 表示以h开头以d结尾的字符串
# n9 = re.fullmatch(r'h.*d', 'hello world')
# print(n7)
# print(n8)
# print(n9)
# print('-' * 30, '关于fullmatch')
#
# # 关于re.Match类
# x = re.search(r'm', 'o3regmsdxvb')
# # . 任意字符 * 任意次数
# x1 = re.search(r'm.*a', 'o3rtegmsdxavb')

# -----------------------------------08-正则表达式(re.Match类中的方法)--------------------------------------------------

# # 关于pos 和 endpos
# # 打印开始查找的位置和结束查找的位置
# print(x.pos, x.endpos)
#
# # 关于span()
# # 返回匹配结果开始位置和结束位置的下标
# print(x1.span())
# print('-' * 30, '关于span()')
#
# # 关于group
# # 使用group返回匹配到的结果 group可以传参， 参数表示第几个分组
# # group表示正则表达式的分组
# # 在正则表达式里使用一个小括号表示一个分组 如果没有分组，默认只有一个组 分组从下标0开始
# print(x1.group())
# print(x1.group(0))
#
# # 分组0：(9.*)(0.*)(5.*7) 第0组是把整个正则表达式当成一个分组 默认情况下是第0组
# # 分组1：(9.*)
# # 分组2：(0.*)
# # 分组3：(5.*7)
# m1 = re.search(r'9.*0.*5.*7', 'da9sk0ldfjkljxcjv5sdfa7sdkl')
# m2 = re.search(r'(9.*)(0.*)(5.*7)', 'da9sk0ldfjkljxcjv5sdfa7sdkl')
# print(m1)
# print(m2.group(0))  # 9sk0ldfjkljxcjv5sdfa7
# print(m2.group(1))  # 9sk
# print(m2.group(2))  # 0ldfjkljxcjv
# print(m2.group(3))  # 5sdfa7
# print('-' * 30, '关于group()')
#
# # 关于groups
# print(m2.groups())
# print(type(m2.groups()))
# print('-' * 30, '关于groups()')
#
# # 关于groupdict()
# m3 = re.search(r'(?P<first>9.*)(?P<second>0.*)(?P<third>5.*7)', 'da9sk0ldfjkljxcjv5sdfa7sdkl')
# print(m3.groupdict())
# print(m3.groupdict())
# # 可以通过分组名或者下标获取到分组里匹配到的字符串
# print(m3.group('first', 'second'))
# print(m3.group(1, 2))
# print(m3.span('first'))


# -----------------------------------08-正则表达式(re.compile类中的方法)--------------------------------------------------
# 创建一个正则对象
# r = re.compile(f'xy')
# 用正则对象调用re模块中的search方法生成一个re.Match类的对象
# x = r.search('abdcdexyfsdf')
# print(x)
# print('-' * 30, '关于re.compile类中的方法')

# -----------------------------------08-正则表达式(正则修饰符)--------------------------------------------------
# # 关于re.S 忽略换行符
# x = re.search(r'm.*a', 'sadklfm\niasdovnax', re.S)
# print(x)
# # 关于re.I 忽略大小写
# y = re.search('x', 'good Xyz', re.I)
# print(y)
# # re.M 让$限定字符能够匹配到换行
# z = re.findall(f'\w+$', 'I am a boy\n, you are a girl\n, he is a man', re.M)
# print(z)
# print('-' * 30, '正则修饰符')

# -----------------------------------08-正则表达式(正则表达式特殊标点符号)--------------------------------------------------
# # \s 任意的非打印字符
# # 非打印字符是空白字符包括空格换行制表符
# print(re.search(r'\s', 'hello world'))
# print(re.search(r'\s', 'hello\nworld'))
# print(re.search(r'\s', 'hello\tworld'))
#
# # \S 非空白字符
# print(re.search(r'\S', '\t\n  x'))
#
# # 标点符号的使用
# # () 用来表示一个分组
# m = re.search(r'h(\d+)x',  'sh829xkflsa')
# print(m.group(0))
# print(m.group(0)[0])
# m1 = re.search(r'\(.*\)', '(1+1)*5+3')
# print(m1)
# # .表示匹配除了换行以外的任意字符
#
# # [] 用来表示区间 可选项范围
# # [x-y] 表示从x-y的区间，包含x和y
# m2 = re.search(r'f[0-5]+m', 'psdf3m')
# m3 = re.search(r'f[a-h0-5]+m', 'psdfb4c2m')
# mf = re.search(r'f[05d]m', 'psdfb4c2m')
# print(m2)
# print(m3)
# print(mf)
# # |用来表示或者的意思 和 [] 相似但是有区别 [] 表示区间 |表示固定的可选值
# m4 = re.search(r'f(x|p|d)m', 'psdfxm')
# print(m4)
# print(m4.group(1))
# # {} 用来限定前面的元素出现的次数 {n}前面的元素出现n次数
# # {n,} 表示前面的元素出现至少n次以上
# # {,n} 表示前面的要出现在n次以下
# # {m,n} 前面的元素出现m-n次
# print(re.search(r'go{2}d', 'good'))
# print(re.search(r'go{2,}d', 'goooood'))
# print(re.search(r'go{,2}d', 'god'))
# print(re.search(r'go{3,5}d', 'gooood'))
#
# # *表示前面的元素出现任意次数 就是0次及以上等价于{0,}
# re.search(r'go*d', 'gooood')
#
# # +表示前面的元素至少出现一次 等价于{1,}
# print(re.search(r'go+d', 'gooood'))
#
# # ? 规定前面的元素最多出现一次 等价于{,1}
# # ? 将贪婪模式转换为非贪婪模式
# print(re.search(r'go+d', 'god'))
#
# # ^ :表示以指定内容开头 $: 表示以指定的内容结尾
# print(re.search(r'^a.*i$', 'afsaefghdi'))
# print(re.match(f'a.*i', 'afsaefghdi'))
# print(re.search(r'^a.*i$', 'xmbp\nafsaefghdi\ngdxh', re.M))

# -----------------------------------08-正则表达式(正则表达式特殊字母)--------------------------------------------------
# print(re.search(r'x\d+p', 'dbcrx243p'))
# print(re.search(r'x.*\d+p', 'dbcxyz245p'))

# -----------------------------------08-正则表达式(正则表达式正则替换)--------------------------------------------------
#
# # 正则表达式替换相关的方法
# # 把每一个数字换成x
# print(re.sub(r'\d', 'x', 'abc2458'))
# # 把多个数字换成x
# print(re.sub(r'\d+', 'x', 'abc2458'))
#
# p = 'hello34good23'
#
#
# # 把字符串里的数字*2 变成hello68good46
# # 第一个参数是正则规则，第二个参数是新字符或者是一个函数 第三个参数是需要被替换的原字符
# # sub内部在调用方法时会把每一个匹配到的数据以re.Match格式传递过去
# def test(x):
#     y = int(x.group(0))
#     y *= 2
#     return str(y)
#
#
# print(re.sub('\d', test, p))
# -----------------------------------08-正则表达式(正则表达式贪婪模式和非贪婪模式)--------------------------------------------------
# 贪婪模式
# 在正则规则里面默认的是贪婪模式
# 在贪婪模式一个字符限定次数的后面加上一个问号就变成了非贪婪模式
print(re.search(r'aa(\d+?)', 'aa2343ddd').group(1))
print(re.search(r'aa(\d+)?', 'aa2343ddd').group(1))
print(re.search(r'aa(\d{2})?', 'aa2343ddd').group(1))
print(re.search(r'aa(\d{2}?)', 'aa2343ddd').group(1))
print(re.search(r'aa(\d+?)ddd', 'aa2343ddd').group(1))
print(re.search(r'aa(\d+)?ddd', 'aa2343ddd').group(1))
print(re.search(r'aa(\d+?).*', 'aa2343ddd').group(1))
print(re.search(r'aa(\d??).*', 'aa2343ddd').group(1)) # 结果为空
