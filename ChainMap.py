"""
作者   ：bjx
创建时间   ：2020/9/7  10:27 下午 
文件名称   ：ChainMap.PY
开发工具   ：PyCharm
"""
#ChainMap使用
from collections import ChainMap
def ChainMap_p(a,b):
    c = ChainMap(a,b)
    print(c['x'])
    print(len(c))


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
ChainMap_p(a,b)

#分割
import re
def split_test():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    new_line = re.split(r'[;,\s]\s*',line)
    print(new_line)

split_test()
