t = int(input())
while t:
    n = int(input())
    b = list(map(int,input().split()))
    m = len(b)
    b.sort()
    ans = []
    used = 0
    i=0
    while used<m:
        ans.append(b[used])
        i+=1
        used+= n-i
        
    ans.append(10**9)

    for i in ans:
        print(i ,end=' ')
    print('\n')
    t-=1