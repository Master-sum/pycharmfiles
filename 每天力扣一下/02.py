"""
作者   ：bjx
创建时间   ：2020/11/13  12:18 上午 
文件名称   ：02.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""
#第一种先遍历
L = []
nums = [2, 7, 11, 15,1,8]
target = 9
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]+nums[j] == target:
            l = [i,j]
            l.sort()
            if l not in L:
                L.append(l)
print(L)
