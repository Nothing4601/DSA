def ans():
    n = int(input())
    a = list(map(int,input().split()))
    index1 = 1
    index2 = -1
    
    for i in range(1,n,1):
        if a[i]!=a[0]:
            index2 = i+1
            break
    
    if index2==-1:
        print('NO')
        return
    
    print('YES')

    for i in range(1,n,1):

        if a[i]==a[0]:
            print(index2,i+1)

        else: print(index1,i+1)

t =int(input())
while t:
    ans()
    t-=1