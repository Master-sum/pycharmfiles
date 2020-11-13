"""
作者   ：bjx
创建时间   ：2020/11/1  10:03 下午 
文件名称   ：两数之和.PY
开发工具   ：PyCharm
"""
'''
nums = [2,7,11,15]
target = 9
nums[0] + nums[1] = 9
print(0,1)
'''
def sum(L):
    for i in range(len(L)):
        for j in range(i,len(L)):
            s = L[i] + L[j]
            if s == 9:
                print("[{},{}]".format(i,j))




nums = [2,7,11,15,4,5]
sum(nums)