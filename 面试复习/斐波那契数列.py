"""
作者   ：bjx
创建时间   ：2020/12/14  12:26 上午 
文件名称   ：斐波那契数列.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""

import sys
def Fibonacci(n):

    a,b,count = 0,1,0
    while True:

        if(count>n):
            return

        yield a
        a,b = b,a+b
        count+=1

f = Fibonacci(15)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()