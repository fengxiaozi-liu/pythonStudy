"""
异步是迭代器
    实现了__aiter__()和__anext()__方法的对象。
    __anext__方法必须返回一个awaitable对象。
    async_for会处理异步迭代器的__anext__()方法返回的可等待对象，直到其引发一个StopAsyncIteration异常
异步迭代对象
    可在async_for语句中被使用的对象，必须通过它的a__iter__()方法，返回一个asynchronous iterator
"""
import asyncio


class Reader:
    """
    自定义异步迭代器（同时也是异步可迭代对象）
    """

    def __init__(self):
        self.count = 0

    async def readline(self):
        await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    def __anext__(self):
        val = await self.readline()
        if val == None:
            raise StopAsyncIteration
        return val


async def func():
    obj = Reader()
    async for item in obj:
        print(item)


asyncio.run(func())
