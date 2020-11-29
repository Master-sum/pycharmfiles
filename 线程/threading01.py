"""
作者   ：bjx
创建时间   ：2020/11/29  9:34 下午 
文件名称   ：threading01.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import time
import threading

def sayHello():
    print("hello,,,")
    time.sleep(3)

if __name__ == "__main__":
    start = time.time()
    for i in range(5):
        t = threading.Thread(target=sayHello)
        t.start()
    end = time.time()
    print("耗时%0.6f"%(end-start))