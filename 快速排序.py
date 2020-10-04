"""
作者   ：bjx
创建时间   ：2020/10/3  10:14 下午 
文件名称   ：快速排序.PY
开发工具   ：PyCharm
1．先从数列中取出一个数作为基准数。
2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。
"""
#快速排序：采用分而治之

def func(a):
    #判断比较之后list长度是否大于2
    if len(a)<2:
        return a
    mid = a[0]#获取到基准数
    print(mid)
    l = [i for i in a[1:] if i<mid] #获得小于mid的数
    r = [i for i in a[1:] if i>mid] #获得大于mid的数
    return func(l)+[mid]+func(r) #进行递归调用函数
a = [12,34,54,2,3,7,1]
print(func(a))