t = int(input())
while t:
    n , k = map(int,input().split())
    ans = n**k
    print(ans%(10**9+7))

    t-=1
