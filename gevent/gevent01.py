"""
作者   ：bjx
创建时间   ：2020/11/7  9:45 上午 
文件名称   ：gevent01.PY
开发工具   ：PyCharm
"""

import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()



# install -i https://pypi.tuna.tsinghua.edu.cn/simple gevent

