"""
作者   ：bjx
创建时间   ：2020/8/20  12:14 上午 
文件名称   ：getattr.PY
开发工具   ：PyCharm
"""

class Point:
    #初始化
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point{{!r},{!r}}".format(self.x,self.y)

    def add(self,x,y):
        print(self.x+x,self.y+y)

#调用
p = Point(3,4)

#字符串调用
d = getattr(p,'add')(2,3)