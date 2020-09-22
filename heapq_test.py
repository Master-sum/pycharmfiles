"""
作者   ：bjx
创建时间   ：2020/8/13  10:54 下午 
文件名称   ：heapq_test.PY
开发工具   ：PyCharm
"""
#合并多个有序
import heapq
def h_m():
    a = [1,2,3,4]
    b = [6,7,8,9]
    for i in heapq.merge(a,b):
        print(i)

h_m()