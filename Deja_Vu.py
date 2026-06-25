t = int(input())
while(t):
  n,q = map(int,input().split())
  N = list(map(int, input().split()))
  Q = list(map(int, input().split()))
  min_ = 31
  for i in Q:
      if i<min_:
          min_=i
          for j in range(n):
            if N[j] % 2**i==0:
               N[j] +=2**(i-1)
  for i in N:
      print(i,end=' ')
  print('\n')
  t-=1