"""
作者   ：bjx
创建时间   ：2020/8/27  10:14 上午 
文件名称   ：编程1.PY
开发工具   ：PyCharm
"""
"""
yield from打开双向通道，把最外层的调用方与最内层的子生成器连接起来，这样二者可以直接发送和产出值，还可以直接
传入异常，而不用在位于中间的协程中添加大量处理异常的样板代码。有了这个结构，协程可以通过以前不可能的方式委托职责。
1、yield和yield from的区别在于后者可以省去一些循环操作
"""

def num():
  print("我是yield")
  for i in range(10):
      yield i
def num1():
    print("我是yield from")
    yield from range(10)
a = list(num())
print(a)
b = list(num1())
print(b)