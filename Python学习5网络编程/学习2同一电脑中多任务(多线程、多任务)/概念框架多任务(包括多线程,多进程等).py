"""
多任务同时进行
    采用三种方式 多线程 多进程 多线程和多进程

多线程：
    创建多线程：
        import threading
        对象名 = threading.Thread(target=子线程,name=线程名字)
        对象名.start() 开始执行这个线程
    多线程的开发：
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
                锁对象名 = threading.Lock()
                锁对象名.acquire() 加上一个同步锁
                锁对象名.release() 释放这个锁
    线程间通信
        线程之间需要通信，操作系统提供了很多机制来实现线程之间的通信 我们用的最多的是队列Queue
        Queue原理
            Queue是一个先进先出的队列，主进程中创建一个Queue对象，并作为参数传入子进程，两者之间通过put()放入数据
            通过get()取出数据，执行了get()函数之后队列中的数据会被同时删除
        使用：
            队列对象名 = queue.Queue()
            队列对象名.put(data) 将一个数据放入队列里面
            队列对象名.get() 从队列里面获取一个数据同时队列中的数据会被删除一个
多进程：
    程序：
    例如一个xxx.py 这是程序 是静态的
    进程：
        一个程序运行起来后，代码+用到的资源称之为进程，它是操作系统分配资源的基本单元
        不仅可以通过线程完成多任务 进程也是可以的
    进程中的状态：
        工作中， 任务数往往是大于cpu的核数，即一定有一些任务正在执行，而另一些任务在等待CPU的执行，因此导致了有不同的状态
        就绪态：运行的条件都已满足，正等待cpu执行
        执行态：cpu正在执行其他功能
        等待态：等待某些条件满足，例如一个程序sleep，此时就处于等待状态
    创建进程：
        multiprocess模块就是跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象，这个对象可以理解为是一个独立进程
        可以执行另外的事情
        import multiprocessing
        进程对象名 = multiprocessing.Process(target=函数名，name='进程名',args=(参数，...))
        进程对象名.start()
        其中args是传入函数里面的参数
    进程间通信：
        使用multiprocessing中的Queue
        队列对象名 = multiprocessing.Queue()
        需要注意的是q在传入的过程中要作为参数传入每一个进程对象之内
    进程池
        定义：
            当创建的子进程的数量过多达到上百甚至上千的时候，手动创建进程就会使工作量增大，这时候可以用到multiprocessing模块提供的Pool方法
        关于Pool方法：
            初始化Pool方法，可以指定一个最大进程数，当有新的请求提交到Pool中，如果池还没有满，那么就会创建一个新的进程来执行该请求，但是如果池
            中的数量已经达到最大值，那么该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务
进程和线程的区别：
    功能的不同：
        进程： 进程能够完成多任务是完成不同不同程序之间的多任务， 比如一台电脑上可以同时运行多个qq，也可以在运行QQ的同时运行微信
        线程： 线程也能完成多个任务但是是同一个程序的多个任务，比如一个QQ中的多个聊天窗口
    定义的不同：
        进程: 进程是系统进行资源分配和调度的一个独立单位
        线程: 线程是进程的一个实体，是CPU调度和分配的基本单位，它是比进程更小的能独立运行的基本单位，线程自己基本上不拥有系统资源
             只拥有一点在运行中必不可少的资源（如程序计数器，一组寄存器和栈），但是它可与同属于一个进程的其他线程共享进程所拥有的全部资源
    区别：
        一个程序至少有一个进程，一个进程至少有一个线程
        线程的划分尺度小于进程（资源比进程小），使得多线程的并发性高
        进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大的提高了程序的运行效率
        线程不能够独立运行必须依附在进程中
        可以将进程理解为工厂中的一条流水线，而其中的线程就是工人
    优劣势：
        进程 ：更有利于资源的管理和保护但是花费的资源多
        线程： 线程正好相反，线程执行开销小，但是不利于资源的管理与保护

多线程和多进程里面的queue
    线程间通信用到的queue：
        导入多线程里面的queue
            import queue
            队列对象名 = queue.Queue()
        队列对象名.put(data，block=True,timeout=n) 将数据放进队列里面
                block=True表示是阻塞的，如果队列已经满了就不往里面放数据了
                timeout=n 表示等待n秒之后就会报错
        队列对象名.put_nowait(data) 表示不等待直接放，如果放满之后就直接报错
        队列对象名.get(block=True，timeout=n) 从队列里面取出一个数据
                block=True表示是阻塞的，如果队列已经全拿完了就等待
                timeout=n 表示等待n秒之后就会报错
        队列对象名.get_nowait(data) 表示不等待直取，如果取完之后就直接报错
        队列对象名.isfull() 判断队列是否满了
    进程里面的queue
        导入进程里面的queue
            import multiprocessing
            队列对象名 = multiprocess.Queue(n)
            其中n是创建队列时的最大长度，默认值是0表示不限
        队列对象名.put(data，block=True,timeout=n) 将数据放进队列里面
                block=True表示是阻塞的，如果队列已经满了就不往里面放数据了
                timeout=n 表示等待n秒之后就会报错
        队列对象名.put_nowait(data) 表示不等待直接放，如果放满之后就直接报错
        队列对象名.get(block=True，timeout=n) 从队列里面取出一个数据
                block=True表示是阻塞的，如果队列已经全拿完了就等待
                timeout=n 表示等待n秒之后就会报错
        队列对象名.get_nowait(data) 表示不等待直取，如果取完之后就直接报错
        队列对象名.isfull() 判断队列是否满了

线程和进程中的join方法：


"""
# ---------------------------------多任务(多线程)----------------------------------------
# import threading, time
#
#
# def dance():
#     for i in range(10):
#         time.sleep(0.2)
#         print('正在跳舞')
#
#
# def sing():
#     for i in range(10):
#         time.sleep(0.2)
#         print('正在唱歌')
#
#
# # 创建一个线程1 target需要的是一个函数，用来指定线程需要执行的任务
# t1 = threading.Thread(target=dance)
# # 创建一个线程2
# t2 = threading.Thread(target=sing)
#
#
# # 启动线程
# t1.start()
# t2.start()
# ---------------------------------多任务(多进程)----------------------------------------
# import multiprocessing, time, os
#
#
# def dance(n):
#
#     for i in range(n):
#         time.sleep(0.5)
#         print(f'跳舞的pid{os.getpid()}')
#
#
# def sing(n):
#     for i in range(n):
#         time.sleep(0.5)
#         print(f'唱歌的pid{os.getpid()}')
#
#
# p1 = multiprocessing.Process(target=dance, args=(100,))
# p2 = multiprocessing.Process(target=sing, args=(100,))
#
# if __name__ == '__main__':
#     print(f'主进程的pid{os.getpid()}')
#     p1.start()
#     p2.start()

# ---------------------------------多任务(多进程里面的进程池)----------------------------------------
# import multiprocessing, os, random, time
#
#
# def worker(msg):
#     t_start = time.time()
#     print(f'{msg}开始执行，进程等号为{os.getpid()}')
#     time.sleep(random.random() * 2)
#     t_stop = time.time()
#     spend_time = t_stop - t_start
#     print(f'{msg}执行完毕，花费了{spend_time}秒')
#
#
# if __name__ == '__main__':
#
#     # 创建一个进程池，每次规定最大进程为4
#     po = multiprocessing.Pool(4)
#     # 假定执行10个任务
#     for i in range(10):
#         # Pool.apply_async(要调用的目标函数,(传递给目标的参数,要以元组的形式传入))
#         po.apply_async(worker, (i,))
#
#     print('-----start------')
#     po.close()  # 关闭po，关闭后不再接受新的请求
#     po.join()  # 等待po中所有子进程执行完成，必须放在close语句后面
#     print('----end----')

# ---------------------------------多任务(线程和进程里面的join方法)----------------------------------------
import time
import threading

x = 10


def test(a, b):
    time.sleep(1)
    global x
    x = a + b
    return x


# test(1, 2)
# print(x)

t1 = threading.Thread(target=test, args=(1, 1))
t1.start()
print(x)  # 主线程里面立马要结果，因此就把x打印了 这样结果就是10

# 调用join方法 join方法是让主线程等待子线程执行完毕后，主线程才获取到结果
t2 = threading.Thread(target=test, args=(1, 2))
t2.start()
t2.join()
print(x)  # 这样主线程等待完毕之后得到的结果就是子线程执行完了之后的结果
