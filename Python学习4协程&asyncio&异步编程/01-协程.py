"""
协程：
    协程不是计算机提供的，程序员人为的创造的
    协程，也可以称之为微线程，是一种用户动态内的上下文切换技术，简而言之，其实就是通过一个线程实现代码块相关切换执行
怎么实现协程：
    使用第三方的模块greenlet
        早期模块
    通过yield关键字也可以实现协程
    还可以使用asyncio（装饰器）
    通过关键字async, await关键字
协程的意义是什么：
    在一个线程中如果遇到io等待的时间，线程不会等待，利用io等待的时间去执行其他的操作
"""

# 1.使用greenlet实现协程
# from greenlet import greenlet
#
#
# def func1():
#     print('1')  # 第2步：输出1
#     gr2.switch()  # 第3步，切花func2函数
#     print('2')  # 第6步，输出2
#     gr2.switch()  # 第7步，切换到func2
#
#
# def func2():
#     print('3')  # 第4步输出3
#     gr1.switch()  # 第5步，切换到func1
#     print('4')  # 第8步，输出4


# gr1 = greenlet(func1)  # 基于func1生成一个协程对象
# gr2 = greenlet(func2)  # 基于func2生成一个协程对象
# gr1.switch()  # 第1步去执行func1

# 2.通过yield关键字实现协程

# # 如果一个函数里面存在yield关键字，那么他就是一个生成器函数，只要执行这个函数，他就会返回一个生成器
# def func1():
#     yield 1
#     yield from func2()
#     yield 2
#     print(6)
#
#
# def func2():
#     yield 3
#     yield 4
#
#
# f1 = func1()
# for item in f1:
#     print(item)

# 3.通过asyncio实现协程，这个模块就是专门用来实现协程的
# import asyncio
#
#
# # 当我们用这个装饰器装饰了这个函数之后，一般的实现函数的方式就不能够进行
# # 而是通过建立一个循环事件，将每一个任务放到循环事件里面去执行
# @asyncio.coroutine  # 3.8版本之后不支持这种装饰器的使用
# def fun1():
#     print(1)
#     yield from asyncio.sleep(2)  # 遇到耗时操作会自动的切换到其他的task任务当中去
#     print(2)
#
#
# @asyncio.coroutine  # 3.8后不支持这种装饰器
# def func2():
#     print(3)
#      # 遇到io请求可以自动的切花
#     yield from asyncio.sleep(2)  # 同理，遇到耗时操作自动的切换到其他的task任务中去
#     print(4)
#
#
# task = [
#     asyncio.ensure_future(fun1()),
#     asyncio.ensure_future((func2()))
# ]
# loop = asyncio.get_event_loop()  # 创建一个事件循环
# loop.run_until_complete(asyncio.wait(task))  # 将每一个任务放到事件循环里面去

# 4.通过async和await关键字来实现协程，推荐到家使用这种方式，在python3.5之后采用这种方式
import asyncio


# 加上一个async关键字来让函数变成协程函数
async def fun1():
    print(1)
    # 在遇到耗时阻塞的时候，必须使用await关键字，手动挂起阻塞
    await asyncio.sleep(2)  # 遇到耗时操作会自动的切换到其他的task任务当中去
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)  # 同理，遇到耗时操作自动的切换到其他的task任务中去
    print(4)


task = [
    asyncio.ensure_future(fun1()),
    asyncio.ensure_future((func2()))
]
loop = asyncio.get_event_loop()  # 创建一个事件循环
loop.run_until_complete(asyncio.wait(task))  # 将每一个任务放到事件循环里面去
