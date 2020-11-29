"""
作者   ：bjx
创建时间   ：2020/11/29  6:15 下午 
文件名称   ：queue.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import os,time,random
from multiprocessing import Process,Queue

def write(q):
    for v in ['a','b','c']:
        print(v)
        q.put(v)
        time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            v = q.get(True)
            print(v)
            time.sleep(random.random())
        else:
            break

if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print("end")