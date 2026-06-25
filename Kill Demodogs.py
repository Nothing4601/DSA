t = int(input())
while t:
    n= int(input())
    ans = (n*(n+1)*(2*n + 1))//6 + ((n-1)*(n)*(n+1))//3
#     for i in range(1,n+1,1):
#           ans+= (i-1)*i + i**2
#           ans = (ans*2022)%(10**9+7)
    print((ans*2022)%(10**9+7))
    t-=1