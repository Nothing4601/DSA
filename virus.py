t = int(input())
while t:
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    infected = m
    a.sort()
    gap = [] # edge case m==1

    for i in range(1,m,1):
        gap.append(a[i] - a[i-1]-1)
    gap.append( (n-a[-1]) + (a[0] -1) ) # last element as house are circular
    
    gap.sort(reverse=True)

    for i in range(m):
        if (gap[i] - 4*i) > 0:

            if (gap[i] - 4*i)==1:
                 infected+=4*i

            else:infected+=4*i + 1

        else: infected += gap[i]
       
    print(infected)
    
    



    t-=1