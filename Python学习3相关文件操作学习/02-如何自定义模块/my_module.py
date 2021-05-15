a = 'hello'
m = 'yes'
n = 100


def test():
    print('我是my_module模块里的函数')


def foo():
    print('我是my_module模块里面的foo方法')


def division(a, b):
    return a / b


# 测试__name__方法
if __name__ == '__main__':
    print('demo里的name是', __name__)
    print('测试division', division(4, 2))
