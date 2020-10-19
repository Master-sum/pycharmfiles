"""
作者   ：bjx
创建时间   ：2020/10/19  10:32 上午 
文件名称   ：猴子补丁.PY
开发工具   ：PyCharm
猴子补丁是动态属性替换，在程序运行时修改类或者模块
"""
class monkey:
    def hello(self):
        print("hello")
    def world(self):
        print("world")

def temp():
    a = 1
    print(a)

m = monkey()
#把函数原本的执行的功能给替换了
m.hello = m.world
m.world = temp

m.hello()#world
m.world()#1