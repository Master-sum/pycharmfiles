
"""
作者   ：bjx
创建时间   ：2020/8/11  11:00 下午 
文件名称   ：password.PY
开发工具   ：PyCharm
"""
import itertools as its

words = "0123456789"

r = its.product(words,repeat=5)

dic = open(r"/Users/baijinxing/Documents/files/pass.txt","a")

for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
    print(i)
dic.close()
