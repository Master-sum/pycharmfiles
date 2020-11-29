"""
作者   ：bjx
创建时间   ：2020/11/29  9:41 下午 
文件名称   ：threading02.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import threading
import time
# 唱歌函数
def sing():
    for i in range(10):
        print("sing...%d"%i)
        time.sleep(2)
#跳舞函数
def dance():
    for i in range(10):
        print("dance...%d"%i)
        time.sleep(2)

if __name__ == "__main__":
    print("---开始---:%s"%time.ctime())
    # 创建线程对象t1,并执行功能函数
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    # 启动线程
    t1.start()
    t2.start()
    # 当前线程阻塞，直到t1结束
    t1.join()
    t2.join()
    print("---结束----：%s"%time.ctime())