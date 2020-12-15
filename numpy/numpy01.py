"""
作者   ：bjx
创建时间   ：2020/12/14  12:32 上午 
文件名称   ：numpy.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import numpy as np
import xlwings as xw
# 初始化
wb = xw.Book()
sht = wb.sheets[0]
info_title = [
    ['21','hello','shanghai'],
    ['22','hello','shanghai']
]
title = [['title','world','crity']]
sht.range('a1').value = title
sht.range('a2').value = info_title
wb.save('/Users/baijinxing/Documents/files/t.xlsx')