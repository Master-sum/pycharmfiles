"""
作者   ：bjx
创建时间   ：2020/8/26  12:36 下午 
文件名称   ：yield_and_yield_from.PY
开发工具   ：PyCharm
"""
def y(*args,**kwargs):
    for item in args:
        for i in item:
            yield i


def y_f(*args,**kwargs):
    for item in args:
        yield from item#可以迭代对象

if __name__ == "__main__":
    astr = "abcd"
    alist = [1,2,3,4,5,6]
    adict = {'name':'bjx','agr':19,'sex':'man'}
    l = y(astr,alist,adict)
    l_f = y_f(astr,alist,adict)
    print(list(l))
    print(list(l_f))