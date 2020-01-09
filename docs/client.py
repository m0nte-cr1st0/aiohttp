# from mylib.traceconfig import AuditRequest
import asyncio, aiohttp
#
#
# async def some_function():
#     async with aiohttp.ClientSession() as client:
#         await client.get('http://example.com/some/redirect/')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(some_function())
# loop.close()


async def read_website():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://example.org/') as resp:
            await resp.read()

loop = asyncio.get_event_loop()
loop.run_until_complete(read_website())
# Zero-sleep to allow underlying connections to close
loop.run_until_complete(asyncio.sleep(0))
loop.close()