def same_partity(a,b):
    return (abs(a-b)%2==0)
t= int(input())
while t:
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    pre_sum=[]
    pre_sum.append(a[0])
    
    for i in range(1,n,1):
        pre_sum.append(pre_sum[i-1] + a[i])
    if t==1:print('second test case',pre_sum)
    while q:
        l,r,k = map(int,input().split())
        curr_sum = pre_sum[l-2] + (r-l+1)*k + (pre_sum[-1] - pre_sum[r-1])
        if t==1:print('second test case qury',curr_sum)
        print('Yes') if curr_sum%2!=0 else print('No')
        q-=1
    t-=1
