t = int(input())
def a():
    a,b,n = map(int,input().split())
    if a<b:
         print('1')
         return
    length = min(b,a/n)
    if length == b:
       print('1')
       return
    elif b==a:
       print('1')
       return
    else:
       print('2')
       return
while t:
    a()
    # for i in range(n):
    #     m = n-i
    #     length = min(b,a/m)
    #     if length==b:
    #       if i==0:
    #         print('1')
    #         break
    #       if b==a/m and i==n-1:
    #          print('1')
    #          break
    #       else:
    #         print('2')
    #         break
    #     if a<b:
    #         print('1')
    #         break
    t-=1