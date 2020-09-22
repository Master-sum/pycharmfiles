"""
作者   ：bjx
创建时间   ：2020/8/27  12:23 上午 
文件名称   ：上下文io.PY
开发工具   ：PyCharm
"""
#判断输入是否为闰年
def run(y):
    if y%4 == 0 and y%100 != 0 :
        print("%d是闰年"%y)
        if y%400 == 0:
            print("%d是世纪闰年" % y)
        else:
            print("%d不是世纪闰年" % y)
    else:
        print("%d不是闰年" % y)



if __name__ == "__main__":
    y = int(input("请输入年份"))
    run(y)