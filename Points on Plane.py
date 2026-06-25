import math
t = int(input())
while(t):
    n=int(input())
    ans = int(math.sqrt((n-1)))
    if (ans+1)*(ans+1) < n:
        ans=ans+1
    print(ans)
    t=t-1