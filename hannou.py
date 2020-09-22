"""
作者   ：bjx
创建时间   ：2020/8/13  10:33 下午 
文件名称   ：hannou.PY
开发工具   ：PyCharm
"""
def hannuo(n,A,B,C):
    if n == 1:
        print(A+"-->"+C)
    else:
        hannuo(n-1,A,C,B)#第一个递归是将A柱上最底下移动到C
        print(A + "-->" + C)
        hannuo(n-1,B,A,C)#第二个递归是将B柱上的移动到C柱

if __name__ == "__main__":
    hannuo(3,"a","b","c")