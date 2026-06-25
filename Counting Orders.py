t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort(reverse=True)
    a.sort(reverse=True)
    j = 0
    ans = 1
    for i in range(n):
        while (j<n) and (b[i]< a[j]) :
            j+=1
        # a[j] is equal or less than b[i]
        if j-i<=0:
            ans = 0
            break
        ans = (ans * (j-i)) % (10**9 + 7)
  
    print(ans)
    t-=1