"""
作者   ：bjx
创建时间   ：2020/8/17  10:50 下午 
文件名称   ：str_repr.PY
开发工具   ：PyCharm
"""
#str和repr的区别
class p:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'p1({0.x!r},{0.y!r})'.format(self)

    def __str__(self):
        return 'p({0.x!r},{0.y!r})'.format(self)

p1 = p(3,4)
print(p1)