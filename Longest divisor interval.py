t= int(input())
while t:
  n = int(input())
  ans =1
  i=2
  while n%i == 0:
    ans+=1
    i+=1
  print(ans)
  t-=1