"""
作者   ：bjx
创建时间   ：2020/8/24  11:14 下午 
文件名称   ：set_list.PY
开发工具   ：PyCharm
"""
#利用set函数
def s_list(l):
    a = set(l)
    print(a)
#使用正常对比
def s_l(l):
    d = []
    for i in range(len(l)):
        for j in range(i+1,len(l)):

            if l[i] == l[j]:
                print(l[i], l[j])
                del l[j]
                return l





l = [1,2,3,1,3,4,5,6,5]
print(s_l(l))
