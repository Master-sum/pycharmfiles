"""
作者   ：bjx
创建时间   ：2020/11/14  10:46 上午 
文件名称   ：07.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
'''
Z 字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N

输入: s = "LEET CO DEIS HI RING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''
'''
思路：
1、获取规则：凡事算法都存在规则
2、第一个行3行时间隔3个元素，第二行间隔3个元素，第三行间隔3个元素；当行数是4时，第一行间隔5个，第二行5个...


s = "LEET CO DEIS HI RING"
'''
s = "LEETCODEISHIRING"
s_l = list(s)
s1 = ''
numRows = 4

# for i in range(numRows):
#     y = []
#     L.append(y)
# spacing = numRows - 2
# it = len(s)/numRows
# for j in range(0,int(it)):
#     t = j*numRows
#     if t ==0:
#         s1 += s[t:t+numRows]
#     else:
#         s1 += s[t+j*spacing:t+j*spacing+numRows]
# print(s1)
# 暴力算法
L = []
f = int(numRows/2)
for i in range(0,numRows):
    l = []
    for j in range(0,numRows-1):
        if i==1 and j>0:
            t = j * 6
            next = i + t-2
            l.append(s_l[next])
            l.append(s_l[i + t])
        elif i==2 and j>0:
            t = j * 6
            next = i + t - 4
            l.append(s_l[next])
            l.append(s_l[i + t])
        else:
            t = j*6
            l.append(s_l[i + t])
    L.append(l)

for k in L:
    s1+= ''.join(k)
print(s1)


