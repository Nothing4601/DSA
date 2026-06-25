def gcd(m,n):
    if m==0:
        return n
    elif n==0:
        return m
    else:
        return gcd( min(m,n), max(m,n) % min(m,n) )

t = int(input())
while t:
    n =int(input())
    a = list(map(int,input().split()))
    
    ans  = abs(a[0]-a[-1])
    for i in range(1,n//2,1):
        ans = gcd(ans, abs(a[i] - a[-1-i]))
    print(ans)
    t-=1