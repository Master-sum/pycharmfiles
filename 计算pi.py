"""
作者   ：bjx
创建时间   ：2020/8/27  12:45 上午 
文件名称   ：计算pi.PY
开发工具   ：PyCharm
"""
#pi = 4(1+(3^-1)*(-1)^1
def pi():
    sum = float(0)
    for i in range(1,1000):
        s = ((2**i)-1)

        sum += float(s**(-1)*(-1)**(i-1))

    pi = 4 * sum
    print("%f"%pi)

pi()