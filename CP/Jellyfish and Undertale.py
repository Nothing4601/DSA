t= int(input())
while t:
    a,b,n = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        ans+=min(a-1,x[i])
    print(ans+b)
    t-=1