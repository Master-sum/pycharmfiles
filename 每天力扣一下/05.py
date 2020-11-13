"""
作者   ：bjx
创建时间   ：2020/11/13  2:33 下午 
文件名称   ：05.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
1、
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
2、
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
'''
nums1 = [1,2]
nums2 = [3,4]
nums1.extend(nums2)
new_l = sorted(nums1)
print(new_l)
if len(new_l)%2 != 0:
    l = len(new_l)/2
    z = int(l)+1
    z_data = new_l[z]
    print("中位数%d"%z_data)
else:
    l = len(new_l) / 2
    z1 = int(l)- 1
    data = new_l[z1]
    data1 = new_l[int(l)]
    sum_d = (data1+data)/2
    print("中位数%f" % sum_d)
