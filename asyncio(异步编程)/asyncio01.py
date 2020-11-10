"""
作者   ：bjx
创建时间   ：2020/11/6  1:53 下午 
文件名称   ：asyncio.PY
开发工具   ：PyCharm
"""
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    await say_after(3,'python')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
print("----test2---")

# test2
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    tesk3 = asyncio.create_task(say_after(3,'python'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    await  tesk3

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
print("test3")



import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())