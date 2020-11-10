import asyncio

async def nested():
    return 42
async def nested1():
    return 421
# Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    task1 = asyncio.create_task(nested())

    # Let's do it differently now and await it:
    print(await nested())  #协程

    print(await nested1()) #任务
asyncio.run(main())