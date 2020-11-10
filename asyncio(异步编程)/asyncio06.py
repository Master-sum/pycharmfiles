"""
作者   ：bjx
创建时间   ：2020/11/7  12:44 下午 
文件名称   ：asyncio.PY
开发工具   ：PyCharm
"""
import asyncio

async def test1():
    print("请等待20s")
    await asyncio.sleep(2)


async def main():
    try:
        await asyncio.wait_for(test1(),20)
        print("正常访问")
    except Exception as e:
        print("超时{}".format(e))


asyncio.run(main())

