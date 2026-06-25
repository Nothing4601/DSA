import math
t =int(input())
while(t):
    l,r=map(int,input().split())
    ans=int(math.sqrt((r-l+1)*2))
    if(ans*(ans+1)< (r-l+1)*2): # make sure no equality
        print(ans+1)
    else:
      print(ans)
    t=t-1