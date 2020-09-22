"""
作者   ：bjx
创建时间   ：2020/8/18  10:17 下午 
文件名称   ：Person.PY
开发工具   ：PyCharm
"""
class Person:
    def __init__(self,name):
        self.name = name
    @property
    def name(self):
        print(self._name)

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("Ex")
        self._name = value
    @name.deleter
    def name(self):
        raise AttributeError("can't deleter ")

#继承Person类
class Superson(Person):

   @property
   def name(self):
       print("g")
       return super().name

   @name.setter
   def name(self,value):
       print("setting name",value)
       super(Superson, Superson).name.__set__(self,value)

   @name.deleter
   def name(self):
       print("deleter name")
       return super(Superson, self).name.__delete__(self)

s = Superson("gg")
s.name

