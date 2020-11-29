"""
作者   ：bjx
创建时间   ：2020/11/29  4:35 下午 
文件名称   ：进程.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import os
rpid = os.fork()
if rpid<0:
    print("fork fila")
elif rpid==0:
    print("我是子进程{},我是父进程{}".format(os.getpid(),os.getppid()))
else:
    print("我是子进程{},我是父进程{}".format(os.getpid(), rpid))

print("11")
'''
1、os.getpid()是获取当前进程的进程编号
2、os.getppid()是获取当前进程的父进程编号
'''