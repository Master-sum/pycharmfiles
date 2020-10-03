"""
作者   ：bjx
创建时间   ：2020/10/3  5:11 下午 
文件名称   ：希尔排序.PY
开发工具   ：PyCharm
"""
#希尔排序：插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。主要是步长的变化

def func(a):
    n = len(a) #获取list长度
    g = int(n/2)#获取步长
    print(g)
    while g>0: #判断list存在数据
        for i in range(g,n): #在list中间开始往后查找
            temp = a[i] #将数据暂时存放
            j = i
            while j >= g and a[j-g] >temp:#步长之间相减之后获取一个差值进行比较，符合条件之后
                a[i] = a[j-g] #数据交换
                j -= g
            a[j] = temp #进行交换数据
        g = int(g/2) #步长减半
    print(a)

a = [12,34,54,2,3]
func(a)
