"""
作者   ：bjx
创建时间   ：2020/8/23  12:44 上午 
文件名称   ：装饰器使用.PY
开发工具   ：PyCharm
"""
from functools import wraps


# def decorator1(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print("a")
#         return func(*args,**kwargs)
#     return wrapper
#
# def decorator2(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print("c")
#         return func(*args,**kwargs)
#     return wrapper
#
# @decorator1
# @decorator2
# def test():
#     print("b")
#
# if __name__ == "__main__":
#     test()
# def wrapper(*args,**kwargs):
#     print(**kwargs)
#
# wrapper([11,2],{"q":"1"})



l = [12,123,1253,3464,34]
l1 = []
l2 = []
l3 = {}
l4 = ''
for i in l:
    s = str(i)
    d = int(len(s))
    l1.append(d)
for j in l1:
    k = 10**j
    l2.append(k)

new = zip(l,l2)
p = list(new)

for f in p:
    g = f[0]/f[1]
    l3[g] = f[0]
res =sorted(l3.items(),key=lambda x:x[0],reverse=True)
for key,value in res:
     s = str(value)
     l4 += s
print(l4)


