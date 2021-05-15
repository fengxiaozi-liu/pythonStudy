"""
第一个：异步操作redis
    在通过代码操作redis时，链接/断开/操作都是网络io
"""
import asyncio
import aioredis
import aiomysql


# 异步操作redis
# async def execute(address):
#     print('开始执行')
#     # 网络io操作创建redis连接
#     redis = await aioredis.create_redis(address)
#     # 在redis里面设置哈希值car
#     await redis.hmset_dict('car', key1=1, key2=2, key3=3)
#     # 去redis中获取值
#     result = await redis.hgetall('car', encoding='utf-8')
#     print(result)
#     redis.close()
#     # 关闭redis连接
#     await redis.wait_closed()
#     print('结束', address)
#
#
# asyncio.run(execute('127.0.0.1'))

# 用异步的方式连接mysql
# async def execute(address, password, database):
#     # 异步连接mysql
#     coon = await aiomysql.connect(host=address, password=password, db=database, user='liu', charset='utf8')
#     # 异步创建游标
#     cursor = coon.cursor()
#     # 异步查询数据库
#     await cursor.execute('select * from student')
#     # 异步获取全部的数据
#     await cursor.fetchall()
#     # 异步关闭游标
#     await cursor.close()
#     coon.close()
#
# asyncio.run(execute('localhost', 'lh284259', 'python_study'))
