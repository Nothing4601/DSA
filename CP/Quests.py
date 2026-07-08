t = int(input())
while(t):
    n,k = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    curr_sum = a[0] + (k-1)*b[0]
    ans = curr_sum
    b_max = b[0]
    pre_b_max = b[0]

    for i in range(1,min(k,n),1):
        if b[i] > b_max:
            pre_b_max = b_max
            b_max=b[i]
        else:
            pre_b_max=b_max
        
        curr_sum = curr_sum + a[i] + (k-1-i)*b_max - (k-i)*pre_b_max
        ans=max(ans,curr_sum)
    print(ans)
    t-=1