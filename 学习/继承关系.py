"""
作者   ：bjx
创建时间   ：2020/11/9  11:43 上午 
文件名称   ：继承关系.PY
开发工具   ：PyCharm
"""
class Md(dict):
    def my(self,key,value):
        super().my(key,[value]*2)


dd = Md(one=1)
print(dd)
dd['t'] = 2
print(dd)
