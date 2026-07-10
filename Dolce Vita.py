def fun_():
    n, budget  = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    pref_sum = [0]*n
    pref_sum[0] = a[0]

    for i in range(1,n,1):
        
        pref_sum[i]= pref_sum[i-1] + a[i]
    
    ans = 0
    pre_day = -1
    
    if pref_sum[0]> budget:
         print('0')
         return
    
    for packets in range(n,0,-1): # as we can buy max n packet on particular day
        # find max days such that (pref_sum[n-1] - budget)//j is greather than or equl to days
        days = -1
        l=0
        r=10**9
        while l<=r:
            
            mid = (l+r)//2
         #   print(f'l {l} r{r} and days {days}')
            if (pref_sum[packets-1] + mid*packets)<= budget:
                      l=mid+1
                      days=mid
            else:
                 r=mid-1

        #print(f"days {days}, prev days = {pre_day}, packets {packets} over all sum{pref_sum[packets-1] + days*packets}" )

        ans+= (days - pre_day)*packets
        pre_day = days
        
        
    print(ans)

t = int(input())
while t:
    fun_()
    t-=1