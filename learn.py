"""
作者   ：bjx
创建时间   ：2020/10/4  11:24 上午 
文件名称   ：learn.PY
开发工具   ：PyCharm
"""

# import threading
# import time
#
# sem = threading.Semaphore(7)
# def func():
#     if sem.acquire():   #也可以用with进行上下文管理
#         print(threading.current_thread().getName()+"get semaphore")
#         time.sleep(2)
#         sem.release()
#
# for i in range(20):
#     t1 = threading.Thread(target=func)
#     t1.start()

#lambda匿名函数
#函数式编程
def func():
    dict = {'a':24,'g':52,'I':12,'k':33}
    d =  dict.items()
    c = sorted(dict.items(),key=lambda x:x[1])
    print(d)
    print(c)

#反转字符串
def func1():
    s = "wbxuxu"
    s1 = s[::-1]
    print(s1)
#list排序
def func2():
    list1 = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':24},{'name':'d','age':27}]
    l = sorted(list1,key=lambda x:x['age'],reverse=False)
    print(l)

def func3():
    list1 =[1,2,3,4]
    list2 = [4,5,6,7]
    set1 = set(list1)
    set2 = set(list2)
    print(set1&set2)#相同元素
    print(set1^set2)#不同元素

func3()