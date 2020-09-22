"""
作者   ：bjx
创建时间   ：2020/9/6  10:14 下午 
文件名称   ：笛卡尔积.PY
开发工具   ：PyCharm
"""
#使用list推导式
def cartesian():
    colors = ['black', 'white']
    size = ['S', 'M', 'L']
    tshirts = [(c,s) for c in colors for s in size]
    print(tshirts)
cartesian()