"""
作者   ：bjx
创建时间   ：2020/11/29  4:42 下午 
文件名称   ：pool_use.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import os
import time,random
# 引入进程池
from multiprocessing import Pool
# 函数
def worker(msg):
    start = time.time()
    print("{}开始执行，进程编号{}".format(msg,os.getpid()))
    time.sleep(random.random()*2)
    end = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(end-start))
# 运行方法
if __name__ == "__main__":
    # 定义进程大小
    po = Pool(3)
    # 执行次数
    for i in range(10):
        # 调用目标函数
        # po.apply_async(worker,(i,))
        po.apply(worker,(i,))

    print("--start_-----")
    po.close()
    po.join()
    print("---end--")

'''
apply和pply_async的区别是
'''