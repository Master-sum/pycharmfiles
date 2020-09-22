"""
作者   ：bjx
创建时间   ：2020/8/25  11:44 下午 
文件名称   ：mytests.PY
开发工具   ：PyCharm
"""
#使用类导入模式

from C3 import singleton
#__new__创建单例模型
class Singleton(object):
    #定义一个私有变量
    _instance = None
    #__new__创建一个对象,__init__函数初始化
    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
a = Singleton()
b = Singleton()
print(a == b)#值相同
print(a is b)#引用地址相同
singleton.foo()
#装饰器版本
from functools import wraps
#创建一个装饰器
def Singleton(cls):
    #定义一个字典
    instance = {}
    @wraps(cls)
    def getinstance(*args,**kwargs):
        #判断这个类是否存在于字典中
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        print(instance)
        return instance[cls]
    return getinstance
@Singleton
class Myc(object):
    b = 1
m = Myc()

#使用元类的版本
class Singleton(type):
    #定义一个私有变量
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton,cls).__call__(*args,**kwargs)
            return cls._instance[cls]

class My(metaclass=Singleton):
    print("11")
t = My()
print(t)



