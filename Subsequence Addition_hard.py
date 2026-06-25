def fun():
    n =int(input())
    c = list(map(int, input().split()))
    c.sort()
    if c[0] != 1:
        print('NO')
        return
    sum = 1
    for i in range(1,n,1):
        if sum < c[i]:
            print('No')
            return
        sum += c[i]
    print('Yes')

t  = int(input())
while t:
    fun()
    t-=1