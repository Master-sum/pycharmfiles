"""
作者   ：bjx
创建时间   ：2020/11/1  10:15 下午 
文件名称   ：两数相加.PY
开发工具   ：PyCharm
"""
"""
输入：2->4->3 + 5->6->4
输出: 7—>0->8
原因:342+465 = 807  
"""
import re
str1 = input("输入：")
data = str1.split('+')
path = re.compile('\d+')
la = []
for i in data:
    d = path.findall(i)
    s = ''.join(d)
    s1 = s[::-1]
    la.append(s1)
sum1 = int(la[0])+ int(la[1])
sd = str(sum1)
print("输出:{}—>{}->{}".format(sd[-1],sd[1],sd[0]))
print("原因:{}+{} = {}".format(la[0],la[1],sum1))

