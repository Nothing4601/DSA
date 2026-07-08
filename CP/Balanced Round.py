t= int(input())
while t:
    n,k  = map(int,input().split())
    a = list(map(int,input().split()))
    max_conti = 1
    ans = 1
    a.sort()
    for i in range(1,n,1):
        if (a[i] - a[i-1])<=k:
           max_conti+=1
           ans = max(max_conti,ans)
        else:max_conti=1
    print(n-ans)
    t-=1