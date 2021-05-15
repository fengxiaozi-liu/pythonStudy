"""
在异步爬虫里面有一个future对象它是对任务的封装
在python自带的模块中有concurrent.futures.Future对象它是基于线程创建的异步
将同步操作变成异步操作的方法：
    future = loop.run_in_executor(None, requests.get, url)
        -loop.run_in_executor就是让一个同步操作变成异步操作
            第一个参数可以是ThreadPoolExecutor/ProcessPool/None 表示是基于线程池还是基于进程池，None默认是线程池
            第二个参数是指定变成异步操作的函数
            第三到第n个参数是要传递给函数的的参数
    response = await future
        -上一步变成了异步操作，同时也变成了一个协程对象，可以使用await关键字进行挂起

    上面的操作合并起来就是await loop.run_in_executor(None, requests.get, url)

    注意：在使用同步变异步操作的时候要抓住改变的本质是，这个事件是一个耗时操作，我们把它变成异步是为了节省运行时间
"""
import aiohttp
import asyncio
import requests
import time


# 使用异步协程下载图片
# async def picture(url):
#     print('请求开始')
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             content = await response.content.read()
#             name = url.split('/')[-1]
#             with open(name, 'wb') as fp:
#                 fp.write(content)
#
#
# async def main():
#     url_list = ['https://p1.ssl.qhimgs1.com/sdr/400__/t014850ba22dd61f18b.jpg',
#                 'http://pic34.photophoto.cn/20150307/0005018347440631_b.jpg',
#                 'http://img3.100bt.com/upload/ttq/20131213/1386933556075_middle.jpg']
#     task_list = [asyncio.create_task(picture(url)) for url in url_list]
#     await asyncio.wait(task_list)
#
# asyncio.run(main())

# 使用异步协程加python中的线程下载图片
async def download(url):
    print('开始下载', url)
    loop = asyncio.get_event_loop()
    # request模块不支持异步操作，所以就使用线程池配合使用，将requests模块放进线程池里面
    # 将future编程一个协程对象，只有编程了协程对象，才能使用await关键字
    # 将requests对象变成了协程对象，加上await关键字之后requests就从同步操作变成了异步操作
    # future = loop.run_in_executor(None, requests.get, url)
    # 只有等到拿到requests响应对象的时候，才进行下一步操作，所以手动挂起future
    # response = await future

    # 合并
    response = await loop.run_in_executor(None, requests.get, url)
    print('下载完成开始保存图片')
    name = url.split('/')[-1]
    content = response.content
    with open(name, 'wb') as fp:
        # fp.write(content)
        # 将同步操作变成异步操作
        await loop.run_in_executor(None, fp.write, content)
        print('图片保存完成')


async def main():
    url_list = ['https://p1.ssl.qhimgs1.com/sdr/400__/t014850ba22dd61f18b.jpg',
                'http://pic34.photophoto.cn/20150307/0005018347440631_b.jpg',
                'http://img3.100bt.com/upload/ttq/20131213/1386933556075_middle.jpg']
    task_list = [asyncio.create_task(download(url)) for url in url_list]
    await asyncio.wait(task_list)


start = time.time()
asyncio.run(main())
print(time.time() - start)
