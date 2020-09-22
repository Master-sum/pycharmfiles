"""
作者   ：bjx
创建时间   ：2020/8/19  11:58 下午 
文件名称   ：Alternative.PY
开发工具   ：PyCharm
"""
#状态机来取代if-else
class State:
    #初始化
    def __init__(self):
        self.new_state(State_A)

    #调用类
    def new_state(self,state):
        self.__class__ = state
        print(state.__name__)
    #报错提醒
    def action(self,x):
        raise NotImplementedError


class State_A(State):
    def action(self,x):
        self.new_state(State_B)


class State_B(State):
    def action(self, x):
        self.new_state(State_C)

class State_C(State):
    def action(self, x):
        self.new_state(State_A)


c = State_C()
c.action('C')