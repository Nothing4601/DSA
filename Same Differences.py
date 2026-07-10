t =int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    fre_count = {}
    
    for i in range(n):
        b= a[i] - i
        fre_count[b] = fre_count.get(a[i]-i,0) + 1

    ans = 0
    for i in fre_count:
        f = fre_count[i]
        ans+= (f*(f-1))//2
    print(ans) 
    t-=1