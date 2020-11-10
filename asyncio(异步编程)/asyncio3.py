"""
作者   ：bjx
创建时间   ：2020/11/6  2:49 下午 
文件名称   ：asyncio3.PY
开发工具   ：PyCharm
"""
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)



import time


# 定义异步函数
async def hello():
    asyncio.sleep(1)
    print('Hello World:%s' % time.time())

def run():
    for i in range(5):
        # 将 loop 设置为当前 OS 线程的当前事件循环
        loop.run_until_complete(hello())
# 获取当前事件循环

if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    run()