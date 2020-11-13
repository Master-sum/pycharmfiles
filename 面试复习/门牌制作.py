"""
作者   ：bjx
创建时间   ：2020/10/29  10:12 下午 
文件名称   ：门牌制作.PY
开发工具   ：PyCharm
"""
"""
大概就是说制作门牌号是一个一个数字网上贴的，
比如1017需要2个1，1个0，1个7。然后问你制
作1到2020一共需要多少个数字2
"""

s=0
for i in range(1,2021):# 遍历1到2020
    s+=str(i).count('2')# 查找有多少个2
# print(s)
'''
一个小孩，从2000年1月1日到2020年10月10日每天都跑1千米，
而周一或月初（每月1号）他会跑2千米。如果既是周一也是月初
也是跑2千米。问他一共跑了多少千米。
'''
from collections import Counter
str = "longlonglongistoolong"
c = Counter(str)
d = c.items()
e = sorted(d,key=lambda x:x[1])
f = len(e)
g = e[f-1]

print(g[0],g[1])
