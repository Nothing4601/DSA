t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    operations = 0
    last_ele = a[-1]
    conti =1
    i=n-1
    while i>=1:
      if a[i-1]==last_ele:
         conti+=1
         i-=1
      else:
         operations+=1
         i=i-conti
         conti*=2
    print(operations)
    t-=1