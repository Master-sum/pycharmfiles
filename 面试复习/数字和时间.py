"""
作者   ：bjx
创建时间   ：2020/10/22  4:07 下午 
文件名称   ：数字和时间.PY
开发工具   ：PyCharm
"""
"""
import json
dict = {'name':'hello','age':18}
str = json.dumps(dict)
print(str,type(str))#{"name": "hello", "age": 18} <class 'str'>
dict_str = json.loads(str)
print(dict_str,type(dict_str))#{'name': 'hello', 'age': 18} <class 'dict'>
"""
"""
l = [1,2,3,5]
l.reverse()#[5, 3, 2, 1]
print(l)
s = 'ssss11'
print(s[::-1])#11ssss
class A:
    p = 12
    def tt(self):
        print("www")
    @staticmethod
    def tes():
        print('hello')
    @classmethod
    def tes2(cls):
        st = cls.p
        print(st)
A().tt()
A().tes()
A().tes2()
"""
"""
#pickle序列化成二进制
import pickle
d=dict(name='wc',age=28)
t = pickle.dumps(d)#将字典行转str
#函数enumerate使用，可以将索引位标记出来
s = ['he','ll','o','world']
c = enumerate(s)
for i in c:
    print(i)
    '''
    (0, 'he')
    (1, 'll')
    (2, 'o')
    (3, 'world')
    '''
#isnumeric()检查是否含有数字
#isalpha()检查是否含有字母
#检查是否含有数字和字母isalnum()
"""
"""
def fun(num):
    try:
       num<4
    except:
        print('11')
    finally:
        print('exit')#退出之后执行

fun(5)
"""
"""
l = [1,4,3,3,32,2,22,4,2,26]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        continue
    print(l1)
"""
"""
def func(x):
    if x == 0:
        return 1
    else:
        return x * func (x-1)

print(func(8))

s = {i:i*i for i in range(8)}
print(s)
"""
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#  return 'Hello World!'
# if __name__ == '__main__':
#  app.run(debug=True)
# l=[1,2,3,4,5]
# def f(i):
#   return  i*i
# d = map(f,l)
# c = list(d)
# e = [i for i in c if i>10]
# print(e)
# a = lambda x,y:x*y
#
# print(a(2,3))
# dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# l = sorted(dic.items(),key=lambda x:x[0],reverse=False)
# print(l)
# from collections import Counter
# s ="sxsnsjnxsxjs"
# l = Counter(s)
# print(l)
# a = "not 404 found 张三 99 深圳"
# s = a.split(" ")
# p = []
# import re
# path = re.compile(r'([0-9a-z]+)\s+')
# d = re.findall(path,a)
# print(d)
# for i in s:
#  if i not in d:
#     p.append(i)
#
# print(p)
# #filter()过滤函数
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def fun(x):
#    return x%2 == 1
# f = filter(fun,a)
# print(list(f))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s = [i for i in a if i%2==1]
# print(s)
# a = [1,5,7,9]
# b = [2,2,6,8]
# a.extend(b)
# print(a)

#异常代码raise
# def func(n):
#  try:
#   for i in range(n):
#    if i>5:
#     raise Exception("xnjsnxs")
#  except Exception as e:
#   print(e)
# func(7)
# import re
# a="张明 98分"
# s = re.sub('98','100',a)
# print(s)
# def func(k,v):
#  dict = {}
#  dict[k] = v
#  print(dict)
# func('a','d')
# dic={"name":"zs","age":18}
# #del dic['name']
# dic.pop('name')
# print(dic)
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# d = sorted(foo,key=lambda x:(x<0,abs(x)))
# print(d)
#列表嵌套字典的排序，分别根据年龄和姓名排序
# foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
# f = sorted(foo,key=lambda x:x['name'])
# a = sorted(foo,key=lambda x:x['age'])
# print(f,a)
# t = {"name":"zs","age":19}
# # f = zip(t.values(),t.keys())
# # d = {i[0]:i[1] for i in f}
# # print(d)
# f = sorted(t.items(),key=lambda x:x[0])
# print(f)

"""
在100以内输出
12=6+6
100=80+20
# """
# import random
# for i in range(10):
#  a = random.randint(0,100)
#  b = 100 -a
#  if a>b:
#   s = a - b
#   print("{}={}-{}".format(s,a,b))
#  else:
#   s = a+b
#   print("{}={}+{}".format(s, a, b))
# str='12'
# list = []
# for i in str:
#  list.append(int(i))
#  print(list)
# def lengthOfLongestSubstring(s):
#  i = j = l = 0
#  k = []
#  for j, c in enumerate(s):
#   if c in s[i:j]:
#    print(s[i:j])
#    t = s[i:j]
#    print(len(t))
#    k.append(len(t))
#    l = max(l, len(s[i:j]))
#    i += s[i:j].index(c) + 1
#  print(max(k))
# lengthOfLongestSubstring('abcecabcabc')

'''
import threading
import time
def music(name):
   for i in range(2):
       print("music")
       time.sleep(5)
def movie(name):
   for i in range(2):
        print("movie")
        time.sleep(5)
threads = []
t1 = threading.Thread(target=music,args=(u'梁祝',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u'卧虎藏龙',))
threads.append(t2)
if __name__ == '__main__':
   for t in threads:
        t.setDaemon(True)
        t.start()
print("finish")
'''
# b1=[1,2,3]
# b2=[2,3,4]
# b3 = [val for val in b1 if val in b2]
# print (b3)
#!/usr/bin/env python
# coding=utf-8
