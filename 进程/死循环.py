"""
作者   ：bjx
创建时间   ：2020/12/13  11:03 下午 
文件名称   ：死循环.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import threading,multiprocessing
# 计算出电脑CPU个数
cpu_num = multiprocessing.cpu_count()
print(cpu_num)
# 循环体
def loop():
    x = 0
    while True:
        x = x^1

for i in range(cpu_num):
    t = threading.Thread(target=loop)
    t.start()