"""
作者   ：bjx
创建时间   ：2020/10/1  6:54 下午 
文件名称   ：10.1.PY
开发工具   ：PyCharm
"""
#冒泡排序
# def func(a):
#     a = list(set(a))#去重
#     for i in range(len(a)):
#         for j in range(i,len(a)):
#             if a[i] > a[j]:#比较之后进行交换
#                 min = a[j]
#                 a[j] = a[i]
#                 a[i] = min
#     print(a)
#
# a = [5,2,6,7,1,3,3]
# func(a)
#快速排序
# def func(a):
#     a = list(set(a))
#     for i in range(len(a)):
#         minindex = i
#         for j in range(i,len(a)):
#                 if a[j] < a[minindex]:
#                     minindex = j
#
#         tepm = a[i] #寻找最小的数
#         a[i] = a[minindex] #将最小数的索引保存
#         a[minindex] = tepm
#
#     print(a)
#
# a = [5,2,6,7,1,3,3]
# func(a)
#插入排序,对无序的数据进行扫描之后插入

