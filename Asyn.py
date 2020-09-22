"""
作者   ：bjx
创建时间   ：2020/8/16  10:35 下午 
文件名称   ：Asyn.PY
开发工具   ：PyCharm
"""
from functools import wraps
from queue import Queue
import multiprocessing

def app_ay(func,args,*,callback):
    result = func(*args)
    #回调函数
    callback(result)
class Any:
    #初始化函数
    def __init__(self,func,args):
        self.func = func
        self.args = args

#装饰器
def intt(func):
    @wraps(func)
    def wrapper(*args):
        r = func(*args)
        res_q = Queue()
        res_q.put(None)
        while True:
            result = res_q.get()
            try:
                a = r.send(result)
                app_ay(a.func, a.args, callback=res_q.put)
            except StopIteration:
                break


    return wrapper


def add(x,y):
    return x+y
@intt
def test():
    r = yield Any(add,(2,3))
    print(r)
#加入线程池
if __name__ == "__main__":

    pool = multiprocessing.Pool()
    app_ay = pool.apply_async

    test()

