"""
作者   ：bjx
创建时间   ：2020/11/12  5:57 下午 
文件名称   ：快手一面算法.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
"""
算法题：给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：

[

 [-1, 0, 1],

 [-1, -1, 2]

]
"""
"""
1、思路三次遍历
"""
import  numpy as np
st = []
L= []
nums = [-1, 0, 1, 2, -1, -4]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        for k in range(j,len(nums)):
            #这里将所有的三次循环放到list
            p = [i,j,k]
            #去重防止取到同一个数字
            g = set(p)
            if len(g)==3:
                d = nums[i]+nums[j]+nums[k]
                if d==0:
                    l = [nums[i],nums[j],nums[k]]
                    #将每次的三元组进行排列
                    l.sort()
                    if l not in st:
                        st.append(l)

#换行输出
x = np.array(st)
print(x)
'''
按顺序指定一个元素，然后取两个游标元素，向中间移动，查找满足条件的三元组。
第一个游标的起始位置是指定元素后一个元素，第二个游标的起始位置是最后一个元素。
时间复杂度为O(n^2)。
'''

