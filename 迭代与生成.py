"""
作者   ：bjx
创建时间   ：2020/8/25  10:28 下午 
文件名称   ：迭代与生成.PY
开发工具   ：PyCharm
"""
def yi():
    l = [x*x for x in range(10)]
    print(l)
    g = (x*x for x in range(10))
    print(g.__next__())
    print(g.__next__())
yi()
