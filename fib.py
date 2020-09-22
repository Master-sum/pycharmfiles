
#斐列波函数
def fib_num(n):

    if n <= 1:

        return n
    else:
        #此处不能相加，值得思考（2020年8月10号）
        return fib_num(n-1) + fib_num(n-2)#回调函数


#输入数字
def input_num():
    str = input("请输入一个正整数")
    try:
        n = int(str)
    except ValueError as e:
        print("请输入正整数")
        input_num()
    return n
#主函数调用
if __name__ == "__main__":
    n = input_num()
    print("第{}项的值{}".format(n,fib_num(n)))