t = int(input())
while t:
  n = int(input())
  a = list(map(int,input().split()))
  if a[0]==-1 and a[n-1]!=-1:
    a[0] = a[n-1]
  elif a[0]!=-1 and a[n-1]==-1:
    a[n-1] = a[0]
  elif a[0]==-1 and a[n-1]==-1:
    a[0]=a[n-1]=0
  
  print(abs(a[n-1]-a[0]))
  for i in range(n):
    if a[i]==-1:
      print('0',end=' ')
    else :print(a[i], end=' ')
  print('\n')
  t-=1