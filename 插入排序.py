"""
作者   ：bjx
创建时间   ：2020/10/3  3:08 下午 
文件名称   ：插入排序.PY
开发工具   ：PyCharm
插入排序：算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
1、获取整个list的长度，之后依次取后面的数据往前面有序的数据中插入
"""
def func(a):

    for i in range(1,len(a)):
        index = i-1 #获取前一个数
        tp = a[i] #将该数据保存
        while(index>=0 and a[index]>tp): #当index是正数且前一个数大于后一个数时进行插入操作
            a[index+1] = a[index]#将前一个数往后移动
            index = index-1#再将该数和前面的比较
        a[index+1] = tp#最后将值插入进去
    print(a)
a = [5,2,6,7,1,3]
func(a)