"""
作者   ：bjx
创建时间   ：2020/9/19  3:43 下午 
文件名称   ：registy.PY
开发工具   ：PyCharm
"""
registy = []
def registy_t(func):
    print("执行函数{}".format(func.__name__))
    registy.append(func)
    return func
@registy_t
def f1():
 print('running f1()')
@registy_t
def f2():
 print('running f2()')
def f3():
 print('running f3()')
def main():
 print('running main()')
 print('registry ->', registy_t)
 f1()
 f2()
 f3()
if __name__=='__main__':
 main()