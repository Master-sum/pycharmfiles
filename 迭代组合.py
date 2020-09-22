"""
作者   ：bjx
创建时间   ：2020/8/26  4:57 下午 
文件名称   ：迭代组合.PY
开发工具   ：PyCharm
"""
#itertools模块的使用
from itertools import permutations

def permu(item):
    for p in permutations(item):
        print(p)

item = ['a','b','c']

permu(item)
#enumerate使用
def en(e):
    for n,(x,y) in enumerate(e):
        print(n,(x,y))

e = [(1,2),(3,4),(5,6)]
en(e)