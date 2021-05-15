import multiprocessing, threading
import os

n = 100


def test():
    global n
    n += 1
    print(f'{os.getpid()}n的值是{n}')


def demo():
    global n
    n += 1
    print(f'{os.getpid()}中n的值是{n}')


# 创建两个线程，查看线程对全局变量的影响
# 一个进程里面的多个线程共享全局变量
t1 = threading.Thread(target=test, name='线程1')
t2 = threading.Thread(target=demo, name='线程2')

# 创建两个进程查看进程对全局变量的影响
# 不同的进程各自保存一份全局变量 不共享全局变量
m1 = multiprocessing.Process(target=test, name='线程1')
m2 = multiprocessing.Process(target=test, name='线程2')

if __name__ == '__main__':
    t1.start()
    t2.start()
    m1.start()
    m2.start()
