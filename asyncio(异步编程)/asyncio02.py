"""
作者   ：bjx
创建时间   ：2020/11/6  2:38 下午 
文件名称   ：asyncio02.PY
开发工具   ：PyCharm
"""
import asyncio
import time
#定义一个函数
async def test(delay,what):
    await asyncio.sleep(delay)
    print(what)
#定义一个异步函数
async def mian():
    # asyncio.create_task()创建一个并发的机制
    task1 = asyncio.create_task(test(2,'hello'))
    task2 = asyncio.create_task(test(3,'world'))
    print(f"strat {time.strftime('%X')}")
    #等待，可以等待的类型有协程, 任务 和 Future
    await task1
    await task2
    print(f"end {time.strftime('%X')}")

asyncio.run(mian())#执行主函数