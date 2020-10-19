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

def fibo(n):
    if n ==0:
        n =0
        return n
    if n <= 2:
        n = 1
        return n
    else:
        return fibo(n-1)+fibo(n-2)
list = [fibo(i) for i in range(200)]

print(list)


