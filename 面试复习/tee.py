"""
作者   ：bjx
创建时间   ：2020/11/7  10:22 下午 
文件名称   ：tee.PY
开发工具   ：PyCharm
"""
#11月7下午面试
def add(n,i):

    return n+i

def test():
    for i in range(4):
        print(i)
        yield i

g = test()
l = []
# print(list(g))[0,1,2,3]
# 1[1, 2, 3, 4]
# 2[11,12,13,14]
# 3[16,17,18,19]
for n in [1,10]:



    g = (add(n,i) for i in g)


print(list(g))
