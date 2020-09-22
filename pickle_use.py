"""
作者   ：bjx
创建时间   ：2020/8/13  11:54 下午 
文件名称   ：pickle_use.PY
开发工具   ：PyCharm
"""
#序列化
import pickle
data = 123456789
f = open('somefile','wb')
pickle.dump(data,f)
f = open('somefile','rb')
d = pickle.load(f)
print(d)