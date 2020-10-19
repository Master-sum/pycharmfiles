"""
作者   ：bjx
创建时间   ：2020/10/19  10:40 上午 
文件名称   ：快速排序.PY
开发工具   ：PyCharm
原理：快速排序由于排序效率在同为O(N*logN)的几种排序方法中效率较高，因此经常被采用，
再加上快速排序思想----分治法也确实实用，因此很多软件公司的笔试面试，包括像腾讯，
微软等知名IT公司都喜欢考这个，还有大大小的程序方面的考试如软考，考研中也常常出现快速排序的身影。
基本思想是：
1．先从数列中取出一个数作为基准数。
2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。
"""
'''

def partition(arr, low, high):
    # arr = [10, 7, 8, 9, 1, 5]
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]#

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
    
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    print(111)
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr[i]),
'''

# def quick_sort(lists,i,j):
#     if i >= j:
#         return list
#     pivot = lists[i]#基准数
#     low = i #左边
#     high = j#右边
#     while i < j:
#         while i < j and lists[j] >= pivot:
#             j -= 1
#         lists[i]=lists[j]
#         print(lists)
#         while i < j and lists[i] <=pivot:
#             i += 1
#         lists[j]=lists[i]
#         print(11)
#         print(lists)
#     lists[j] = pivot
#     print(low,i-1)
#     quick_sort(lists,low,i-1)
#     quick_sort(lists,i+1,high)
#     return lists
#
# if __name__=="__main__":
#     lists=[30,24,5,58,18,36,12,42,39]
#     print("排序前的序列为：")
#     for i in lists:
#         print(i,end =" ")
#     print("\n排序后的序列为：")
#     for i in quick_sort(lists,0,len(lists)-1):
#         print(i,end=" ")





def quick(lists,l,h):
    if l >= h:
        return lists
    base = lists[l]
    low = l
    high = h

    while l<h:
        while l<h and lists[h]>= base:
            h -=1
        lists[l] = lists[h]
        while l < h and lists[l] <= base:
            l += 1
        lists[h] = lists[l]
    lists[h] = base
    quick(lists,low,l-1)
    quick(lists,l+1,high)
    return lists

if __name__=="__main__":
    lists=[30,24,5,58,18,36,12,42,39]
    print("排序前的序列为：")
    for i in lists:
        print(i,end =" ")
    print("\n排序后的序列为：")
    for i in quick(lists,0,len(lists)-1):
        print(i,end=" ")


















