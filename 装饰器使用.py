"""
作者   ：bjx
创建时间   ：2020/8/23  12:44 上午 
文件名称   ：装饰器使用.PY
开发工具   ：PyCharm
"""
from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("decorator1")
        return func(*args,**kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("decorator2",func.__name__)
        return func(*args,**kwargs)
    return wrapper

@decorator1
@decorator2
def add(a,b):
    s = a+b
    print(s)

if __name__ == "__main__":
    add(2,3)