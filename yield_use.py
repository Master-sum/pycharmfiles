"""
作者   ：bjx
创建时间   ：2020/8/13  10:43 下午 
文件名称   ：yield_use.PY
开发工具   ：PyCharm
"""
#主要是学习yield生成器
def flatten(item):#此时该函数已经是个生成器，需要迭代
    for i in item:


        yield i #此时i被抛出下一次需要next进行循环

    print(111)
if __name__ == "__main__":
    item = [1,2,3,4]
    for i in flatten(item):
        print(i)