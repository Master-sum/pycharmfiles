#阶乘函数
def fac(n):
    sum = 1
    while n != 1:
        sum = n * sum
        n = n -1
    return sum

print(fac(5))