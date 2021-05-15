import os, multiprocessing
from multiprocessing import Queue


def produce(x, n):
    for i in range(10):
        n += 1
        x.put(f'{os.getpid()}生产b{i}面包')
        print(f'{os.getpid()}生产了b{i}面包，现有面包{n}个')


def customer(x, n):
    for i in range(10):
        y = x.get()
        n -= 1
        print(f'消费了pid{y}，还剩{n}个面包')


q = Queue()
num = 0
m1 = multiprocessing.Process(target=produce, name='进程1', args=(q, num))
m2 = multiprocessing.Process(target=customer, name='进程2', args=(q, num))

if __name__ == '__main__':
    m1.start()
    m2.start()
