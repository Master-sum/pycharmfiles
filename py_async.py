"""
作者   ：bjx
创建时间   ：2020/8/16  10:06 下午 
文件名称   ：py_async.PY
开发工具   ：PyCharm
"""
#传递函数，变量，回调函数
def app_ay(func,args,*,callback):
    result = func(*args)
    #回调函数
    callback(result)

def add(x,y):
    return x+y

def tt(result):
    print("get:",result)

#使用闭包解决状态问题

def handler():
    s = 0
    def h(result):
        #nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量
        nonlocal s
        s += 1
        print("[{}]get:{}".format(s,result))
    return h

h1 = handler()
app_ay(add,(1,3),callback = h1 )