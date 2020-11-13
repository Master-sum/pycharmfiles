"""
作者   ：bjx
创建时间   ：2020/11/13  11:33 上午 
文件名称   ：03.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
import re
str1 = input("输入：")
l = str1.split('+')
sum = 0
for i in l:
    #正则匹配数字
    f = re.findall(r'\d+',i)
    #转换字符串
    num_str = ''.join(f)
    #将字符串逆序转整型
    num = int(num_str[::-1])
    #进行累加
    sum += num
#int转换str
a = str(sum)
#使用'->'进行分割
data = '->'.join(a[::-1])
print("输出：%s"%data)
