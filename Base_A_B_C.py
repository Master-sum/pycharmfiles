"""
作者   ：bjx
创建时间   ：2020/8/17  11:21 下午 
文件名称   ：Base_A_B_C.PY
开发工具   ：PyCharm
"""
class Base:
    @property
    def __init__(self):
        print("Base.__init")

class A(Base):
    def __init__(self):
        Base.__init__
        print("A.__init")

class B(Base):
    def __init__(self):
        Base.__init__
        print("B.__init")

class C(A,B):
    def __init__(self):
        # A.__init__(self)
        # B.__init__(self)
        print("C.__init")

c = C()
print(C.__mro__)