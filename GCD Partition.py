def gcd(a,b):
    if b==0:
        return a
    else: return gcd(b,a%b)

t = int(input())
while t:
    n = int(input())
    a= list(map(int,input().split()))
    sum_ = sum(a)
    pre_sum = 0
    score=1
    # optimal partation is k=2
    for i in range(n-1):
        pre_sum += a[i]
        sum_ -= a[i]
        score = max(score, gcd( pre_sum,sum_ ))
    print(score)
    t-=1