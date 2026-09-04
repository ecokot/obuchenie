import asyncio


async def task(name):
    print(f"{name}: start")
    await asyncio.sleep(1)
    print(f"{name}: end")


# async def main():
#     print("Sequential:")
#     await task("A")
#     await task("B")
#
#     print("---")
#     print("Gather (parallel):")
#     await asyncio.gather(task("A"), task("B"))
#
#     print("---")
#     print("Create_task (parallel):")
#     t1 = asyncio.create_task(task("A"))
#     t2 = asyncio.create_task(task("B"))
#     await t1
#     await t2
#
#
# asyncio.run(main())

async def main():
    print("Start:")
    t1 = asyncio.create_task(task("A"))
    t2 = asyncio.create_task(task("B"))
    await asyncio.sleep(1.5)

asyncio.run(main())
