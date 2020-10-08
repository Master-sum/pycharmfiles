"""
作者   ：bjx
创建时间   ：2020/10/8  9:55 下午 
文件名称   ：单例模型.PY
开发工具   ：PyCharm
单列类：确保一个类只有一个实例
"""
class Singleton(object):
    def __new__(cls, *args, **kwargs):#新建一个对象
        if not hasattr(cls,'_instance'):#判断cls对象中是否含有'_instance'属性
            ob = super(Singleton,cls)
            cls._instance = ob.__new__(cls, *args, **kwargs)
        return cls._instance

class Myclass(Singleton):
    def __init__(self):
        self.a = 1


class Sun(object):
    __instance=None #定义一个类属性做判断
    def __new__(cls):
        if cls.__instance==None:
            #如果__instance为空证明是第一次创建实例
            #通过父类的__new__(cls)创建实例
            cls.__instance==object.__new__(cls)
            return cls.__instance
        else:
            #返回上一个对象的引用
            return cls.__instance
a = Sun()
print(id(a))
b = Sun()
print(id(b))