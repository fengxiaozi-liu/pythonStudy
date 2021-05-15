"""
1.用户名匹配
    要求：
        用户名只能包含数字，字母和下划线
        不能以数字开头
        长度在6到16位范围内
2.密码匹配
    要求：
        不能包含！@#￥%……&*这些特殊的符号
        必须以字母开头
        长度在6-12位的范围内
3.已知test.txt文件中有一下内容：
    1000phone hello Python
    mobileIetrain 大数据
    1000phone java
    mobileIetrain html5
    mobileIetrain 云计算
    要求：
        查找文件中以1000phone开头的语句 并保存在列表中
4.ipv4格式的ip地址匹配
    提示： ip地址的范围是0.0.0.0 - 255.255.255.255
    1位 0-9组成
    2位[1-9][0-9]
    3位 1[0-9][0-9]
        2[0-4][0-9]
        25[0-5]
5.提取用户输入数据中的数值包括正负数，还包括小数 并求和
"""
import re

# # 用户名匹配规则
# user_name = input('请输入您的用户名 ')
# find_user = re.search(r'^\D(\w{5,15})$', user_name)
# if find_user:
#     print(find_user.group())
# else:
#     print('您输入的用户名不正确')

# 密码匹配规则
# passward = input('请输入你想要的密码')
# find_passward = re.search(r'^[A-Za-z][^!@#￥%^&*]{5,11}',passward)
# if find_passward:
#     print(find_passward.group())
# else:
#     print('请输入6-12位的密码要以字母开头不能包含!@#￥%^&*特殊字符')

# 查找文件中以1000phone开头的语句 并保存在列表中
# file = open('test.txt', 'r', encoding='utf8')
# content = file.read()
# test_list = re.findall(r'1000phone.*', content, re.M)
# print(test_list)

# # 查找ipv4的ip地址的匹配
# ip = input('请输入一个合法的ip地址')
# find_ip = re.fullmatch(r'((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5]){1,3}', ip)
# if find_ip:
#     print(find_ip.group())
#     print(find_ip.group(1))
#     print(find_ip.group(2))
#     print(find_ip.group(3))
# else:
#     print(f'您输入的{ip}格式不正确')

num_list = re.finditer(r'-?(0|[1-9]\d*)(\.\d+)?', '-3.14bcd87c65')
print(num_list)
result = 0
for every in num_list:
    every_num = every.group()
    num = float(every_num)
    result += num
print(result)


