"""
作者   ：bjx
创建时间   ：2020/10/7  5:27 下午 
文件名称   ：超市找零.PY
开发工具   ：PyCharm
"""
def func(a,b):
    c = a - b
    func1(c)

def func1(c):
    l = [0.1,0.5,1,5,10,20,50,100]
    l1 = []
    l2 = []
    for i in range(0,len(l)):
        e = int(c/l[i])
        l1.append(e)
    for j in range(0,len(l1)):
        if l1[j] >=1:
            l2.append(l1[j])
    if len(l2) != 0:
        f = min(l2)
        g = l2.index(f)
        n = f * l[g]

        num = c-n
        #print(num)
        print(f,l[g])
        if num !=0:
            func1(num)

func(60,30)
