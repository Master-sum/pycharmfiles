def hello(l):
    i = len(l)
    print(i)
    for a in range(i,-1,1):
        for b in range(i-1,0,-1):
            if l[b-1]>l[b]:
                c = l[b-1]
                l[b-1] = l[b]
                l[b] = c


    print(l)

if __name__ == "__main__":
    l = [7,5,8,9,2,1,3,4,10]
    hello(l)