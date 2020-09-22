"""
作者   ：bjx
创建时间   ：2020/8/26  3:13 下午 
文件名称   ：反向迭代.PY
开发工具   ：PyCharm
"""
#自定义类
class Countdown:
    #初始化函数
    def __init__(self,start):
        self.start = start
    #构建迭代容器
    def __iter__(self):
        n = self.start
        while n >0:
            yield n
            n -=1
    #进行反向迭代
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

def rev(l):
    for i in reversed(l):
        print(i)

l = [5,4,3,2,1]
rev(l)
c =Countdown(10)
for i in c:
    print(i)
