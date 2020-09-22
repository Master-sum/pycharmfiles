"""
作者   ：bjx
创建时间   ：2020/9/11  11:49 上午 
文件名称   ：2.10练习.PY
开发工具   ：PyCharm
"""
#计算圆的体积
import math
def area(r):
    v = (4/3)*math.pi*r**3
    print(v)




#计算书的价格
def price(n):

    p = (24.95*0.4*n) + 1+(n-1)*0.75
    print(p)

#计算时间
def time():
    #慢速
    v1 = 370/1000
    #快速
    v2 = 270/1000
    t = (1600*2*v1) + (4800*v2)

    m = t%60
    print(t,m)

if __name__ == "__main__":
    time()