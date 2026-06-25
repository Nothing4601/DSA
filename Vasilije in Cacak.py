def first_n_sum(n):
    return (n*(n+1))//2

t = int(input())
while t:
    n,k,x = map(int,input().split())
    max_sum = first_n_sum(n) - first_n_sum(n-k)
    min_sum = first_n_sum(k)
    if x>= min_sum and x<= max_sum:
        print('Yes')
    else:print('no')
    t-=1