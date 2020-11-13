"""
作者   ：bjx
创建时间   ：2020/10/28  11:06 下午 
文件名称   ：nowcode.PY
开发工具   ：PyCharm
计算出从你生日之日起到今天一共过了多少天？

普通闰年：公历年份是4的倍数的，且不是100的倍数，为普通闰年（如2004年、2020年就是闰年）。
世纪闰年：公历年份是整百数的，必须是400的倍数才是世纪闰年（如1900年不是世纪闰年，2000年是世纪闰年）。
"""
import time

# 格式化成2016-03-20 11:45:39形式
time1 = time.strftime("%Y %m %d", time.localtime())
a = time1.split(" ")
print(a)
b = input("请输入时间：")
c = b.split(",")
print(c)
d = []#闰年
e =[]#非闰年

for i in range(int(c[0])-1,int(a[0])):

    if i%4==0 and i%100 !=0:
        d.append(i)
    elif i%100==0 and i%400==0:
        d.append(i)
    else:
        e.append(i)

f = [1,3,5,7,8,10,12]
g = [4,6,9,11]
s = -int(a[2])
r = int(a[1])
while r<=12:
    print(r)
    if r in f:
        s+=31
    elif r in g:
        s+=30
    elif r in d:
        s+=29
    else:
        s+=28
    r+=1
k = -int(c[2])
y = int(c[1])
while y<=12:
    print(y)
    if y in f:
        k+=31
    elif y in g:
        k+=30
    elif y in d:
        k+=29
    else:
        k+=28
    y+=1

sum = len(d)*366+len(e)*365+s+k
print(sum)