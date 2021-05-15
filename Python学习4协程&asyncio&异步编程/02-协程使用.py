import aiohttp
import asyncio


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.content.read()
            file_name = url.split('/')[-1]
            with open(file_name, 'wb') as fp:
                fp.write(content)


async def main():
    url_list = ['http://a1.att.hudong.com/52/79/300245751203132333795320912_950.jpg',
                'https://p1.ssl.qhimgs1.com/sdr/400__/t01e498ffcccd479261.jpg']
    tasks = [asyncio.create_task(fetch(url)) for url in url_list]
    await asyncio.wait(tasks)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
asyncio.run(main())
