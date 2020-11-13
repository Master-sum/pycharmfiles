"""
作者   ：bjx
创建时间   ：2020/11/3  1:50 下午 
文件名称   ：正则表达式替换（字符串中数字乘以2）.PY
开发工具   ：PyCharm
"""
import re
# str = "shdebdey12cdh13"


list=[1,2,3,]
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    print(value)
    return str(value * 2)



s = "shdebdey12cdh13"
double(s)
# print(re.sub('(?P<value>\d+)', double, s))