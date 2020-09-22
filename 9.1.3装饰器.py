"""
作者   ：bjx
创建时间   ：2020/8/22  11:09 下午 
文件名称   ：9.1.3装饰器.PY
开发工具   ：PyCharm
"""
#@classmethod调用自身类属性如下
class A:
    bar = 1
    def func(self):
        print("func1")
    @classmethod
    def method(cls):
        print("method")
        print(cls.bar)
        #调用class A的func方法
        cls().func()
# python装饰器的静态装饰
class B:
    @staticmethod #该方法不强求传递函数，声明一个静态函数
    def static():
        print("static")

class C:
    @property#该装饰器负责把一个方法变成一个属性进行调用
    def score(self):
        print(self.s)
        return self.s
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("请输入正确格式")
        if value < 0 or value > 100:
            raise ValueError("成绩不在范围")
        self.s = value
a = A()
a.method()
B.static()
c = C()
c.score = 70#创建成绩值
#获取成绩
c.score