"""
作者   ：bjx
创建时间   ：2020/8/17  10:59 下午 
文件名称   ：urse_fu.PY
开发工具   ：PyCharm
"""
class A:
    def span(self):
        print("A.span")
#此处B继承了A
class B(A):
    def span(self):
        print("B.span")
        super().span()

b = B()
b.span()