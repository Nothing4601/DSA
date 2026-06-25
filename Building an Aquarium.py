def valid_h(h, a, w):
   water=0
   for i in a:
       water +=max(0,h-i)
       if water > w:
          return False
   return True

t =int(input())
while t:
    n,w = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    lower = 1
    higher = max(a) + w
     
    while(lower <= higher):
      mid = (lower + higher)//2
      if valid_h(mid,a,w):
         lower = mid +1
         ans = mid
      else:
         higher = mid-1
    print(ans)
    t-=1