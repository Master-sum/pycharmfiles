"""
作者   ：bjx
创建时间   ：2020/11/12  11:33 下午 
文件名称   ：01.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。


输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
"""
import re
#输入str类型
l = input()
L = []
#正则匹配数据
date= re.findall(r'\d+',l)
#将获取的数据放在arr中
arr = [int(i) for i in date]
middle = int(len(arr)/2)
a, b = 0, 0
for i in range(len(arr)):
    if i%2==0:
        ou = arr[:middle]
        L.append(ou[a])
        a+=1
    else:
       js = arr[middle:]
       L.append(js[b])
       b += 1
print(L)



