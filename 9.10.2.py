"""
作者   ：bjx
创建时间   ：2020/8/23  4:44 下午 
文件名称   ：9.10.2.PY
开发工具   ：PyCharm
"""
import time
from functools import wraps

#此处定义一个装饰器
def timethis(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        r = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
        return r
    return wrapper
class Span:

    @timethis
    def ins(self,n):
        print(self,n)
        while n>0:
            n -= 1


    @classmethod
    @timethis
    def cls_m(cls,n):
        print(cls,n)
        while n>0:
            n -= 1

s = Span()
s.cls_m(1000)

