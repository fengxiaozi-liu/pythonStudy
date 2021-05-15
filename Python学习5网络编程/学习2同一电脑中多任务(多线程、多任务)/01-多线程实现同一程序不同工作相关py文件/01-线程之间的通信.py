"""
线程间通信
    线程之间需要通信，操作系统提供了很多机制来实现线程之间的通信 我们用的最多的是队列Queue

Queue原理
    Queue是一个先进先出的队列，主进程中创建一个Queue对象，并作为参数传入子进程，两者之间通过put()放入数据
    通过get()取出数据，执行了get()函数之后队列中的数据会被同时删除
    使用multiprocess模块中的Queue实现多线程之间的数据传递
"""
import threading
import time, queue

num = 0


def produce():
    global num
    for i in range(5):
        time.sleep(0.5)
        x = threading.current_thread().name + '的面包b'+str(i)
        y = q.put(x)
        num += 1
        print(f'生产了{x}，现在有{num}个')


def customer():
    global num
    for i in range(5):
        time.sleep(1)
        num -= 1
        # q.get 是一个阻塞的方法 如果运行了这个子线程必须要得到这个数据才能进行下一步
        print(f'{threading.current_thread().name}买到了{q.get()},还剩{num}个')


# 创建了一个队列
q = queue.Queue()

# 创建生产商
p1 = threading.Thread(target=produce, name='生产商1')
p2 = threading.Thread(target=produce, name='生产商2')
p3 = threading.Thread(target=produce, name='生产商3')

# 创建消费者
c1 = threading.Thread(target=customer, name='消费者1')
c2 = threading.Thread(target=customer, name='消费者2')

p1.start()
p2.start()
p3.start()
c1.start()
c2.start()

