import math
t=int(input())

while(t):
    n=int(input())
    a=list(map(int,input().split()))
    pre_sum = []
    pre_sum.append(a[0])
    for i in range(1,n,1):
        pre_sum.append(pre_sum[i-1] + a[i])
   
    ans = 0
    for i in range(1, n, 1):       
        if n%i ==0:
           max_= -math.inf
           min_  = math.inf
           for k in range(0,n,i):
              if k!=0:
                max_ = max(max_,pre_sum[k+i-1] - pre_sum[k-1])
                min_ = min(min_,pre_sum[k+i-1] - pre_sum[k-1])
              else:
                 max_= pre_sum[i-1]
                 min_ = pre_sum[i-1]
           curr_ans = abs(max_ - min_) if max_ !=-math.inf else 0
           ans = max(ans,curr_ans) 

    print(ans)
    t-=1