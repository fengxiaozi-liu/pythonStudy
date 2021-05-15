"""
requests模块是第三方的模块，可以用来发送网络连接
    模拟浏览器实现网络的一个功能
"""
import requests

# response = requests.get('http://127.0.0.1:8080')
# # 得到的结果是一个Response对象
#
# # content 指的是返回的结果，是一个二进制
# print(response.content.decode('utf8'))
#
# # text获取的结果是一个文本
# print(response.text)
#
# # 获取到状态码
# print(response.status_code)

# 如果返回的json字符串会解析json字符串

r = requests.get('http://127.0.0.1:8080/demo')
t = r.text
print(t, type(t))
j = r.json()  # 把json字符串解析成Python里面的数据
print(j, type(j))
