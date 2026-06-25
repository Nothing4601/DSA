t= int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    negative = 0
    zeros = 0
    # may be consider a[i] ==0 case 
    for i in range(n):
        if a[i]<0:
            negative+=1
            a[i] = -a[i]
        elif a[i]==0:
            zeros+=1
    a.sort()
    if negative%2 != 0 and zeros==0:
        print(sum(a[1:]) - a[0])
    else:
        print(sum(a))
    t-=1