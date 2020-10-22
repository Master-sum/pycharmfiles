"""
作者   ：bjx
创建时间   ：2020/10/22  11:15 上午 
文件名称   ：数据结构和算法.PY
开发工具   ：PyCharm
"""
#第一题找到最大或最小元素
"""
#找到最大或最小元素 heapq函数
import heapq
num = [1,2,5,7,77,85,3,9,55]
#找到前三个最大的
max_3 = heapq.nlargest(3,num)
#找到前2个最小的
min_2 = heapq.nsmallest(2,num)
print(max_3)#[85, 77, 55]
print(min_2)#[1, 2]
#可以接受key
str_num = [
    {'h':1,'e':2},
    {'h':44,'e':5},
    {'h':11,'e':21},
    {'h':15,'e':22},
    {'h':15,'e':27},
    {'h':11,'e':2}
]
#获取前三个最大的
str_max_2 = heapq.nlargest(2,str_num,key=lambda a:a['h'])
#找到前2个最小的
str_min_2 = heapq.nsmallest(2,str_num,key=lambda a:a['h'])
print(str_max_2)
print(str_min_2)
"""
#第二题字典的排序
"""
#让字典保存有序，collections模块中的OrderedDict，按照添加的顺序
from collections import OrderedDict
import json
d = OrderedDict()
d['hi'] = 2
d['er'] = 4
d['yu'] = 7
d['ww'] = 1
for key in d:
    print(key,d[key])
#变成字典
d_dict = json.dumps(d)
print(d_dict)

#使用zip进行反转
p = {"hi": 2, "er": 4, "yu": 7, "ww": 1}
#获取最小
min_p = min(zip(p.values(),p.keys()))
print(min_p)
new_p = sorted(zip(p.values(),p.keys()))
print(new_p)
"""
#第三题list、dict去重,set()函数
"""
def func(items):
    new_r = set()
    for item in items:
        if item not in new_r:
            yield item#生成器需要list去迭代
            new_r.add(item)
    print(new_r)
items = [1,2,2,5,6,7,3,23,41,1,5]
list(func(items))
#{1, 2, 3, 5, 6, 7, 41, 23}
def func_dict(d,key =None):
    dict_s = set()
    for item in d:
        val = item if key is None else key(item)
        if val not in dict_s:
            yield val
            dict_s.add(val)
"""
#第四题找出集合中元素最多及个数
"""
from collections import Counter
s = "cdscjsndsiniaskalsxsnia"
d = Counter(s)
print(d)
#Counter({'s': 6, 'n': 3, 'i': 3, 'a': 3, 'c': 2, 'd': 2, 'j': 1, 'k': 1, 'l': 1, 'x': 1})
#最多的三个
max_3 = d.most_common(3)
print(max_3)
"""
#第五题从字典提取子集
"""
p ={'s': 6, 'n': 3, 'i': 3, 'a': 3, 'c': 2, 'd': 2, 'j': 1}
k = {key:value for key,value in p.items() if value<2}
print(k)
"""
