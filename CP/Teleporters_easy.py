t = int(input())
while t:
    n,c = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    # generate total cost for each teleporter
    toal_cost = []
    for i in range(n):
        toal_cost.append(i+1+a[i])
    
    toal_cost.sort()
    for i in range(n):
        if toal_cost[i]<=c:
            ans+=1
            c-=toal_cost[i]
    print(ans)

    t-=1