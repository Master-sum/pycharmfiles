"""
作者   ：bjx
创建时间   ：2020/11/7  10:32 上午 
文件名称   ：两张表相连.PY
开发工具   ：PyCharm
"""
# -*- coding: utf-8 -*-
import pandas as pd

df1 = pd.read_csv('/Users/baijinxing/Documents/files/user.csv',encoding='utf-8',delimiter=',', header=None,error_bad_lines=False)#读取第一个文件

df2 = pd.read_csv('/Users/baijinxing/Documents/files/json.csv',encoding='utf-8',delimiter=',', header=None,error_bad_lines=False)#读取第二个文件

print(df1)
