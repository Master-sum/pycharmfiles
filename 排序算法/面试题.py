"""
作者   ：bjx
创建时间   ：2020/10/19  3:32 下午 
文件名称   ：面试题.PY
开发工具   ：PyCharm
"""
# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
# def normalize(name):
#     return name[0].upper()+name[1:].lower()
#
# def normalizeList(inputlist):
#     return list(map(normalize, inputlist))
# a = normalizeList(['adam', 'LISA', 'barT'])
# print(a)

#正则提取http
import functools
import random
import re


html = '''<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta property="qc:admins" content="465267610762567726375" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Python map() 函数 | 菜鸟教程</title>

  <link rel='dns-prefetch' href='//s.w.org' />
<link rel="canonical" href="http://www.runoob.com/python/python-func-map.html" />
<meta name="keywords" content="Python map() 函数">
<meta name="description" content="Python map() 函数  Python 内置函数  描述 map() 会根据提供的函数对指定序列做映射。 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。 语法 map() 函数语法：  map(function, iterable, ...)  参数  function -- 函数 iterable -- 一个或多个序列  返回值 Pyth..">
		
	<link rel="shortcut icon" href="https://static.runoob.com/images/favicon.ico" mce_href="//static.runoob.com/images/favicon.ico" type="image/x-icon" >
	<link rel="stylesheet" href="/wp-content/themes/runoob/style.css?v=1.157" type="text/css" media="all" />	
	<link rel="stylesheet" href="https://static.runoob.com/assets/font-awesome/4.7.0/css/font-awesome.min.css" media="all" />	
  <!--[if gte IE 9]><!-->
  <script src="https://static.runoob.com/assets/jquery/2.0.3/jquery.min.js"></script>
  <!--<![endif]-->
  <!--[if lt IE 9]>
     <script src="https://cdn.staticfile.org/jquery/1.9.1/jquery.min.js"></script>
     <script src="https://cdn.staticfile.org/html5shiv/r29/html5.min.js"></script>
  <![endif]-->
  2333@qq.com
  <link rel="apple-touch-icon" href="https://static.runoob.com/images/icon/mobile-icon.png"/>
  <meta name="apple-mobile-web-app-title" content="菜鸟教程">
  xiaowang@sina.com.cn
</head>"
'''
# #匹配网站连接
# pattern = re.compile(r'[a-zA-Z]+://www[^\s]*[.com|.cn]',re.S)
# #匹配邮箱
# email = re.compile(r'[a-zA-Z0-9]+@[^\s]*.[com|cn]')
# m = re.findall(email,html)
# print(m)
# #and优先级大于or
# def and_or():
#     a = 1 and 2
#     b = 1 or 2
#     c = 1 and 2 or 3
#
#     print(a,b,c)
# and_or()
#斐波那契数列 0、1、1、2、3、5、8、13、21、34
#
# def fibo(n):
#     if n ==0:
#         n =0
#         return n
#     if n <= 2:
#         n = 1
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
# list = [fibo(i) for i in range(200)]
#
# print(list)
# #一行代码求和
# a = sum(range(100))
# print(a)
# #字典的删除和合并
# dict={'name':'hhh','bb':11}
# print(dict)
# del dict['name']
# print(dict)
# dict.update({'name':'hhh'})
# print(dict)


"""
谈谈
python的GIL，简称全局解释器锁，这个锁是干嘛？就是锁住CPU只能线程，这就对于高并发多核的使用很不友好，
目的是：是解决多线程同时竞争程序中的全局变量而出现的线程安全问题，这个是在cpython解释器中
解决的办法有1、引入多进程，2修改解释器，3使用其他语言C，Java
"""
# #list去重并生成list
# lists = [11,2,2,2,3,4,4,5,6,6]
# a = list(set(lists))
# print(a)
"""python2和"python3中rang的区别在于返回值不同；list和对象"""
"""一句话解释装饰器，函数可以作为参数传递"""
# #python日志装饰器
# def log(date):
#     if callable(date):
#         def w(*args,**kwargs):
#             print(date.__name__)
#             return date(*args,**kwargs)
#         return w
#     def te(func):
#         @functools.wraps(func)
#         def w(*args,**kwargs):
#             print("{}  {}".format(date,func.__name__))
#             return func(*args,**kwargs)
#         return w
#     return te
#
# @log
# def tt():
#     print(11)
#
# @log("ww")
# def tr():
#     print(13)
#
# tt()
# tr()
#
#函数闭包
""" 
def 外层函数(参数):
    def 内层函数():
        print("内层函数执行", 参数)

    return 内层函数


内层函数的引用 = 外层函数("传入参数")
内层函数的引用()
"""
# #利用list=[1,2,3,4,5],map输出[1,4,9,16,25],利用推导式筛选大于10的数
# lists = [1,2,3,4,5]
# def func(i):
#     return i*i
# new_lists = list(map(func,lists))
# list_10 = [i for i in new_lists if i>10]
# print(list_10)

# #python打乱顺序函数shuffle
# from random import shuffle
# lists=[1,2,3,4,5]
# random.shuffle(lists)
# print(lists)
# #python内建数据类型
# int
# dict
# list
# tuple
# str
# bool
#简述__new__ 和__init__的区别
"""
__init__初始化方法
__new__构造对象，返回实例对象，——》__init__使用
__init__可以定制实例对象
__new__必须有返回值，__init__不需要返回值


"""

# class Foo(object):
#     '''黄哥python培训，黄哥所写'''
#     price = 50
#
#     def how_much_of_book(self, n):
#         print(self)
#         return self.price * n
#
# foo = Foo()
# print(foo.how_much_of_book(8))
# print(dir(Foo))


#__new__ 单例模式

# class danli:
#     _n = None
#     def __new__(cls, *args, **kwargs):
#         if cls._n  is  None:
#             cls._n = super(danli,cls).__new__(cls)
#         return cls._n
#
#
#
# danli()
# class danli(object):
#     _n = None
#     t = 8
#     def __new__(cls, *args, **kwargs):#__new__的对象或者函数是class自身
#         if cls._n  is  None:
#             cls._n = object.__new__(cls)
#         return cls._n
#
#     def class_dd(self,n):
#         print(id(self))
#         s = self.t+n
#         print(s)
#
#
#
# a = danli()
# b = danli()
# a.class_dd(4)
# print(id(a),id(b))

# #随机生成正数、小数、
#
# import random
# import numpy as np
# res = random.randint(2,7)
# res_l = np.random.randn(6)
# res_p = random.random()
# print(res)
# print(res_l)
# print(res_p)
# # 断言
# try:
#     a = 3
#     assert(a>4)
# except AssertionError as f:
#     print("错误")

#linux 命令 mv find / -name mkdir cd ls top sudo  rm -rf :wq vi :w cat du df chmod kill netstat ifconfig netconfig ping
"""
python可变： list dict
python不可变：tuple int  str
"""

"""
str去重，s = 'xbdxbhwbxkkw' 按大小顺序排列
"""
# s = 'xbdxbhwbxkkw'
# a = set(s)#字典形
# s1 = ''.join(a)
# print(s1)
# a = list(a)#转为list型使用sort排序
# a.sort(reverse=False)#reverse进行升序
# s2 = ''.join(a)
#
# print(s2)
# #匿名函数的使用
# s = lambda x,y:x*y
# print(s(2,4))
#
# #字典按照键值进行排序
# dict = {'name':13,'age':12,'sex':1,'tel':110}
# for j in dict.items():
#     print(j[1])
# list = sorted(dict.items(),key = lambda i :i[0],reverse=False)
# list_last = sorted(dict.items(),key=lambda k:k[1],reverse=True)
# print(list_last)
# print(list)
# new_dict = {}
# for i in list:
#     new_dict[i[0]] = i[1]
#
# print(new_dict)
#统计字符出现的个数
# from collections import Counter
# s = "xbwxwxwnwxwmxwkxmwopwllw2232o9323029dde"
# mun = Counter(s)
# print(mun)
# #正则过滤英文、数字。空白
# s = "nddj 红黑 jsxn 弧度"
# a = s.split(" ")
# print(a)
# #过滤函数filter
# list1 = [1,1,2,3,4,4,3,5,6,7,88]
# list = list(set(list1))
# def func(l):
#     return l%2 == 1
# n = filter(func,list)
# for i in n:
#
#     print(i)
# #两个list合并，extend
# a = [1,2,5,4]
# b = [7,8,4,3,6]
# a.sort(reverse=False)
# print(a)
# a.extend(b)
# a1 = list(set(a))
# print(a1)
# #时间转化
# import datetime
# str1 = str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ' 星期：'+str(datetime.datetime.now().isoweekday())
# print(str1)

# #zip使用
# a = [2,3]
# b = [3,6]
# s = [i for i in zip(a,b)]
# print(s)
# [(2, 3), (3, 6)]
# re.sub用法
# import  re
# s = "ss 90"
# s1 = re.sub('90','100',s)
# print(s1)
# #单列模型
#
# class danl(object):
#     _n = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._n is None:
#             cls._n = object.__new__(cls)
#         return cls._n
#
# a = danl()
# b = danl()
# print(id(a),id(b))
#cookie在客户端和session在服务端
# #any 和all使用
# print(any([1,3,4,'0']))#一真即真
# print(all([1,2,3,'']))#一假即假
# True
# False
# a = (i for i in range(10))
# #a <generator object <genexpr> at 0x108da6580>
# print(a)
#range 和 xrange区别
# for i in range(10):
#     print(i)
# xrange(10)#生成对象
#str去空
# s = " sh bs ww "
# s.lstrip()#左边
# print(s)


