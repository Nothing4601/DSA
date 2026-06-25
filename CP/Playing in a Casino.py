t = int(input())
while t:
    n, m = map(int,input().split())
    cards= [[0]*n for _ in range(m)]

    for k in range(n):
        a = list(map(int,input().split()))
        for j in range(m):
            cards[j][k] = a[j]
    
    ans = 0
    for i in range(m):
         column = sorted(cards[i],reverse = True)

         for j in range(n):
              ans+=(n-2*j - 1)*column[j]

    # if n==1:
    #     ans= 0
    print(int(ans))

    t-=1