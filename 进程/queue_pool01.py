"""
作者   ：bjx
创建时间   ：2020/11/29  9:09 下午 
文件名称   ：queue_pool.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import os,time,random
from multiprocessing import Manager,Pool
# 读函数
def read(q):
    print("read启动{}父进程为{}".format(os.getpid(),os.getppid()))

    for i in range(q.qsize()):
        print("reader从queue获取到消息：%s"%q.get(True))

#         写函数
def writer(q):
    print("read启动{}父进程为{}".format(os.getpid(),os.getppid()))

    for i in "hello world":
        q.put(i)


if __name__ =="__main__":
    print("%s start"%os.getpid())
    # 初始化队列
    q = Manager().Queue()
    # 创建进程池
    po = Pool()
    # 添加到进程
    po.apply(writer,(q,))

    po.apply(read,(q,))
    # 关闭进程池
    po.close()
    # 执行进程池的操作
    po.join()
    print("%s end"%os.getpid())