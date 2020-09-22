"""
作者   ：bjx
创建时间   ：2020/8/26  2:46 下午 
文件名称   ：yield_from.PY
开发工具   ：PyCharm
"""
#子生成器
def a_gen():
    total = 0
    count = 0
    average = 0
    while True:
        n_num = yield average
        if n_num is None:
            break
        count += 1
        total += n_num
        average = total/count
    return count,total,average
#委托生成器
def p_gen():
    while True:
        count,total,average = yield from a_gen()
        print(count,total,average)
#主函数
def main():
    c_av = p_gen()
    next(c_av)
    print(c_av.send(10))
    print(c_av.send(20))
    print(c_av.send(None))


m = main()