t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    i=1
    if a[0]==1:a[0]=2
    while i<n:
      if a[i]%a[i-1]==0:
         if a[i-1]==1:
            a[i-1]=2
            i-=1
         else:
            a[i]=a[i]+1
            i+=1
      else:i+=1
    for i in a:
       print(i,end=' ')
    print('\n')

    t-=1