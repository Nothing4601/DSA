t = int(input())
while t:
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    remain = {}

    for i in range(m):
        remain[i] = 0

    for i in range(n):
        remain[ a[i]%m] += 1
    
    ans =0
    if remain[0]!=0:
        ans+=1
    
    for i in range(1,m//2+1,1):
        x = remain[i]
        y= remain[m-i]
        if x==y and x!=0:
            ans+=1
        else: ans+= abs(x-y)
    print(ans) 
    t-=1