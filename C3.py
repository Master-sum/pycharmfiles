"""
作者   ：bjx
创建时间   ：2020/8/25  11:13 下午 
文件名称   ：C3.PY
开发工具   ：PyCharm
"""
class A():
    def foo1(self):
        print("A")
class B(A):
    def foo2(self):
        pass
class C(A):
    def foo1(self):
        print("C")
class D(B, C):
    pass
class Singleton(object):
    def foo(self):
        print("这是一个单例模式")
singleton = Singleton()
d = D()
print(D.__mro__)
d.foo1()