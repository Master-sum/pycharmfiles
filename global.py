"""
作者   ：bjx
创建时间   ：2020/9/19  4:18 下午 
文件名称   ：global.PY
开发工具   ：PyCharm
"""
b = 6
def learn(a):
    global b
    print(a)
    print(b)
    b = 9

learn(3)
print(b)

