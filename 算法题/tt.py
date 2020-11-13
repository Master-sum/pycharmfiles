"""
作者   ：bjx
创建时间   ：2020/11/12  10:47 下午 
文件名称   ：tt.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""

e = [1,1,2,3,5]
for i in range(len(e)):
    for j in range(i,len(e)):
        if i!=j:
            print(i,j)