t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    fre = {}
    for i in range(n):
        bit_len = a[i].bit_length()
        fre[bit_len] = fre.get(bit_len, 0) + 1
    
    ans = 0
    for i in fre:
        count = fre[i]
        ans += (count*(count-1))//2
    print(ans)
    t-=1