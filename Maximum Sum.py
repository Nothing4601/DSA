t = int(input())
while t:
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = sum(a[-k:])
    curr_sum = ans
    i=1
    lower = 0
    while i<=k and (lower+2) < n:
        curr_sum = curr_sum - a[-1-k+i] + a[lower] + a[lower + 1]
        lower += 2
        ans  = min(ans, curr_sum)
        i+=1
    print(sum(a) - ans)
    t-=1
