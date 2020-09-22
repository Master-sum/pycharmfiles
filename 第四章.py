"""
作者   ：bjx
创建时间   ：2020/9/11  12:29 下午 
文件名称   ：第四章.PY
开发工具   ：PyCharm
"""
import turtle
import math
def bob():
    b = turtle.Turtle()
    print(b)
    turtle.mainloop()


def polygon(t,n,length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)



def circle(t,r):
    circumference = 2*math.pi*r
    n = 50
    length = circumference/n
    polygon(t,n,length)
if __name__ == "__main__":
   circle(6,3)