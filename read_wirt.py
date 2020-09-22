"""
作者   ：bjx
创建时间   ：2020/8/13  11:03 下午 
文件名称   ：read_wirt.PY
开发工具   ：PyCharm
"""
import gzip
def r_w():
   with open(r"test.txt",'wt') as f:
       f.write("1111")
       print("hello",file=f)#将内容输入到指定文件
       f.close()

def r():
    with open(r"test.txt",'rt') as f:
        a = f.read()
        print(a)
        f.close()



r_w()
r()