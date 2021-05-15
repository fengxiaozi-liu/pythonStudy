"""
同步：
    当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制。
    同步就是协调同步，按照预定的先后次序进行。线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁
互斥锁：
    定义：
        互斥锁为资源引入一个状态 锁定\非锁定
        某个线程要更改共享数据是，先将其锁定，此时资源的状态为锁定，其他线程不能修改，直到该线程释放资源，将资源的状态变成非锁定
        ，其他的线程才能再次锁定该资源，互斥锁保证了每次只有一个线程进行的写入操作，从而保证了多线程的情况下数据的正确性。
    使用：
        threading模块中定义了Lock类，可以方便的处理锁定

"""

import threading
import time

ticket = 10

# 创建一把互斥锁
lock = threading.Lock()


def sell_ticket():
    global ticket
    while True:  # 线程1走到了这里 线程2也走到了这里
        # 第一次 线程1和线程2同时进来 线程1进入执行互斥锁的内容 线程2等待
        # 等到线程1释放的时候 线程2执行互斥锁的内容 因为线程1释放了所以它有能执行下面的代码 但是线程2没被释放它进不来sell_ticket函数
        print(f'{threading.current_thread().name},aaaa')
        lock.acquire()  # 加上一个同步锁
        if ticket > 0:
            time.sleep(0.2)  # 线程1  线程2 同时在这里休息
            ticket -= 1  # 线程1 线程2 都走到了这里
            lock.release()
            print(f'线程{threading.current_thread().name}卖了一张票，还剩的票数为{ticket}')
        else:
            print('票卖完了')
            lock.release()
            break


# 多个线程可以共同操作一个全局变量（多个线程共享全局变量）
# 会出现线程安全问题
t1 = threading.Thread(target=sell_ticket, name='线程1')
t2 = threading.Thread(target=sell_ticket, name='线程2')

t1.start()
t2.start()
