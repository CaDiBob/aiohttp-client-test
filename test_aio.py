import aiohttp
import asyncio

conn = aiohttp.UnixConnector(path="./test.sock")


async def foo():
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get('http://xx/foo') as resp:
            async for line in resp.content:
                print(line)


async def starter():
    await asyncio.sleep(2)
    asyncio.ensure_future(foo())
    await asyncio.sleep(2)
    asyncio.ensure_future(foo())
    await asyncio.sleep(10)


loop = asyncio.get_event_loop()
loop.run_until_complete(starter())
