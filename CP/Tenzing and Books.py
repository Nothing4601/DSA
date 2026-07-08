def tenzing_books():
    n,x = map(int,input().split())
    k=0
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    if x==0:
       print('yes')
       return
    for stack in [a,b,c]:
        for j in stack:
          if j|x==x:  
             k = k|j
          else: break
          if k==x:
             print('yes')
             return
    print('no')
t = int(input())
while t:
    tenzing_books()  
    t-=1 