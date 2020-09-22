"""
作者   ：bjx
创建时间   ：2020/8/18  11:39 下午 
文件名称   ：Date.PY
开发工具   ：PyCharm
"""
import time
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        print(cls(t.tm_year,t.tm_mon,t.tm_yday))
d = Date(2020,8,18)
d.today()