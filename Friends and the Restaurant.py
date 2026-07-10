t = int(input())
while t:
    n = int(input())
    spend = list(map(int,input().split()))
    budget = list(map(int,input().split()))

    diff = []

    for i in range(n):
        diff.append(budget[i] - spend[i])

    diff.sort(reverse=True)

    l= 0
    r = n-1
    days = 0

    while l<r:
        if diff[l] + diff[r] >=0:
            days +=1
            l+=1
            r-=1
        else:r-=1

    print(days)
    t-=1