"""
作者   ：bjx
创建时间   ：2020/11/2  9:48 下午 
文件名称   ：web.PY
开发工具   ：PyCharm
"""
# import requests
# url = "https://www.baidu.com/"
# header = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
# response = requests.get(url=url, headers=header)
# html = response.text()
# print(html)
import re

# str = 'a1b2c3'
# l =[]
# late = []
# for i in str:
#     l.append(i)
# print(l)
# for j in range(0,len(l)):
#     if j%2 != 0:
#         if j==1:
#             new_str1 = l[j - 1] * j
#             # print(new_str1)
#         print(j)
#         s = int(j/2)+1
#         new_str = l[j-1]*s
#         # print(new_str)
#         late.append(new_str)
# print(late)
# new_s = ''.join(late)
# print(new_s)
# #货拉拉面试
# str = 'a2b3n5·'
# #正则匹配
# num = re.findall(r'(\d+)',str)
# abc = re.findall(r'([a-zA-Z]+)',str)
# # 数据整合
# dic = zip(num,abc)
# tp = list(dic)
# tatlo_str = ''
# # 循环遍历
# for i in range(len(tp)):
#     n = tp[i][0]
#     str = int(n)*tp[i][1]
#     tatlo_str += str
# #输出结果
# print(tatlo_str)
# 面试题
# from functools import wraps
#
# def t(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("a")
#         reslut =  func(*args, **kwargs)
#         print("c")
#     return wrapper
# @t
# def test(c):
#     print("b")
# c=1
# test(c)
# def rapper(*args, **kwargs):
#     print(*args)
#     print(**kwargs)
#
# rapper([1,2,3,4],{'q':'12','t':'33'})
# rapper([1,2,3,4],{'q':'12','t':'33'})

