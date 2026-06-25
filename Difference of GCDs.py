def fun_():
    n,l,r =  map(int,input().split())
    a = []
    for i in range(1,n+1,1):
        num = ( (l-1)//i +1)*i
        #num = l + (n -1- (l-1)%i)
        if num > r :
            print(num)
            print('No')
            return
        a.append(num)
    print('Yes')
    for i in range(n):
        print(a[i],end=' ')
    return a

t = int(input())
while t:
    fun_()
    t-=1