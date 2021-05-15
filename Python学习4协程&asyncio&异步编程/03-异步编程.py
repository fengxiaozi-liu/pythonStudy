"""
关于事件循环
    理解成为一个死循环，去检测并执行某些代码
关于async和await
    async是保证任务与任务之间是并行的，就是在一个任务中遇到耗时的阻塞操作时，可以跳转到其他的任务
    await是保证在同一任务之间是串行的，就是在遇到await关键字之后，只有等待这一步的操作完成之后，下面的代码才能执行
    因为下面代码的执行需要依赖await关键字里面的返回值。同时，遇到await关键字之后，证明它就是一个耗时的操作，这样协程就会跳转到
    其他的async任务中
    async和await共同完成协程async保证了任务与任务之间共同进行，await保证了同一任务之间执行流程的完整性
关于task对象

"""
# 示例
# import asyncio
#
#
# async def others():
#     print('start')
#     x = await asyncio.sleep(1)
#     print(x)
#     print('end')
#     return '返回值'
#
#
# async def func():
#     print('执行协程函数里面的代码')
#     # await后面跟协程对象、task对象、future对象， 而且协程对象必须使用await关键字挂起，或者放到事件循环里面，不能直接执行
#     # await的使用场景：是下一步的操作需要上一步的执行结果的时候使用await
#     # await是为了保证在同一个任务里面是串行的
#     # async是保证在不同任务之间是并行的
#     response = await others()
#     print('请求结束，返回', response)
#
#
# asyncio.run(func())

import asyncio


async def others():
    print('start')
    await asyncio.sleep(1)
    print('end')
    return '返回值'


# 原始的方法，使用ensure_future + get_event_loop实现异步协程
# task_list = [
#     asyncio.ensure_future(others()),
#     asyncio.ensure_future(others())
# ]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(task_list))

# 原始方法的改进，通过run实现
# 将协程对象放到列表中
task_list = [others(), others()]
done, pending = asyncio.run(asyncio.wait(task_list))
print(done)

# 新的方法，使用 函数+create_task+await+run实现协程
# async def main():
#     print('执行函数代码')
#     task_list = [
#         asyncio.create_task(others(), name='n1'),
#         asyncio.create_task(others(), name='n2')
#     ]
#     # 将列表中的每一个task对象都加到事件循环中去
#     done, pending = await asyncio.wait(task_list)
#     print(done, pending)
#
# # 将main()方法也加到事件循环中去
# # 这样事件循环里面就有三个任务对象，分别是main()协程对象， task1,task2两个任务对象
# asyncio.run(main())