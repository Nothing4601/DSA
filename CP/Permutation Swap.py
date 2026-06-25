def gcd_(a,b): # assume b is small
    if b==0:
        return a
    return gcd_(b,a%b)

t = int(input())
while t:
    n = int(input())
    p = list(map(int,input().split()))
    ans = 0

    for i in range(n):
       ans = gcd_(ans,abs( p[i]- (i + 1) ))
    
    print(ans)
    t-=1
