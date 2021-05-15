"""
什么是uvloop
    是asyncio事件循环的替代方案
    uvloop事件循环>默认asyncio的事件循环
    import asyncio
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLogPolicy()) 加上这一句可以有效的提升事件循环
    但是Windows不支持uvloop
"""