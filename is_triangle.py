"""
作者   ：bjx
创建时间   ：2020/9/13  11:20 上午 
文件名称   ：is_triangle.PY
开发工具   ：PyCharm
"""
def is_tr(a,b,c):
    list1 = []
    list1.append(a)
    list1.append(c)
    list1.append(b)
    print(list1)
    list1.sort()
    a = list1[0]
    b = list1[1]
    c = list1[2]

    if a+b>c:
        print("yes")
    else:
        print("no")

is_tr(1,2,2)