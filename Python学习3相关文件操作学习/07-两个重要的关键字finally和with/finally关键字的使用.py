"""
finally关键字
    最终都会被执行的代码
    注意事项：

"""
# file = open('C:/Users/19693/Desktop/淘宝视频/视频.mp4', 'rb')
# try:
#     while True:
#         content = file.read(1024)
#         if not content:
#             break
#         print(content)
# finally:
#
#     print('文件被关闭了')
#     file.close()


def test(a, b):
    x = a + b
    return x  # 一般return之后函数就会结束
    return 'hello'  # 一般情况下这段代码不会执行，但是在finally语句下可以实现


def demo(a, b):
    try:
        x = a / b
    except Exception as e:
        return e
    else:
        return x
    finally:
        print('good')


print(test(2, 4))
print(demo(1, 2))
