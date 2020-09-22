"""
作者   ：bjx
创建时间   ：2020/9/14  4:52 下午 
文件名称   ：练习10_1.PY
开发工具   ：PyCharm
"""
def nested_sum(L):
    #判断L是否存在list
    length_list = len(L)
    sum1 = 0
    for i in range(length_list):
        t = L[i]
        sum1 += sum(t)

    print(sum1)


#返回第i个元素加前一个元素
def cumsum(t):
    length_list = len(t)
    sum2 = 0
    t1 = []
    for i in range(length_list):
        sum2 += t[i]
        t1.append(sum2)
    print(t1)

#返回除第一和最后一个元素
def middle(t):
    #弹出第一个
    t.pop(0)
    #重新计算list长度
    length_list = len(t)
    #弹出最后一个元素
    t.pop(length_list-1)
    print(t)
#主函数
if __name__ == "__main__":
    L = [1,2,3,4,5]
    # cumsum(L)
    middle(L)
