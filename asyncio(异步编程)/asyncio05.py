"""
作者   ：bjx
创建时间   ：2020/11/7  12:45 上午 
文件名称   ：asyncio05.PY
开发工具   ：PyCharm
"""
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_event_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


asyncio.run(display_date())