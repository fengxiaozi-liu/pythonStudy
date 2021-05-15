"""
判断用户输入的内容是否是数字，如果是数字则转换成数字类型
"""
import re

user_import = input('请输入一段数字 ')

if re.search(r'^\d+(\.?\d+)?$', user_import):
    print(float(user_import))

else:
    print('请输入一个数字')

# 判断下面正则表达式的含义
# ^\D[a-z0-9A-Z_\-]{3,13} 这个正则表达式判断是否是以非数字开头后面的一个字符是够是[]里面的内容，中括号里面的内容出现3-13次
print(re.search(r'^\D[a-z0-9A-Z_\-]{3,13}', 'SH_8'))
# 邮箱的正则表达式
# r'^([A-Za-z0-9_\-\.])+@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$
# 电话号码的正则表达式
# r'^(13[0-9])|(15[0-9])|(17[5|9])|(18[3-7])\d{8}$
# 匹配身份证号
# r'[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|10|11|22)(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'

