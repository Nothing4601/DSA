t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    min_ = 1
    max_ = n
    l=0
    r=n-1
    while l<r:
        if a[l]==min_:
            l+=1
            min_ += 1
        elif a[l]==max_:
            l+=1
            max_ -= 1
        elif a[r]==min_:
            r-=1
            min_+=1
        elif a[r]==max_:
            r-=1
            max_-=1
        else: break
    if l<r:
        print(l+1,r+1)
    else:print('-1')
    t-=1
