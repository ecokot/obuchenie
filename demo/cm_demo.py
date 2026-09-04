import asyncio

async def ticker():
    for i in [0,1,2]:
        yield i
        await asyncio.sleep(0.5)

async def main():
    async for i in ticker():
        print(i)

asyncio.run(main())


