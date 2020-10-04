"""
作者   ：bjx
创建时间   ：2020/10/4  12:20 下午 
文件名称   ：选择排序.PY
开发工具   ：PyCharm
选择排序：首先在未排序序列中找到最小（大）元素，
存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
"""
b = []
def func(a):

    min = a[0]
    for i in range(1,len(a)):
       if min>a[i]:
           min = a[i]

    print(min)#每次循环找到最小的
    b.append(min)#每次找到最小的就把min添加到b中
    a.remove(min)#每次找到最小的就把min从a中删除
    if len(a)==1:#最后一个直接是最大的
        print(a[0])
    if len(a)>=2:#存在两个数的时候可以进行比较
        func(a)

def func1(a):
    if len(a)>=2:
        for i in range(len(a)):
            min = a[i]
            for j in range(i,len(a)):
                if min>a[j]:
                    min = a[j]

            k = a.index(min)
            a[k] = a[i]
            a[i] = min
        print(a)
    else:
        print(a)

a = [5,2,6,7,1,3]
func1(a)



