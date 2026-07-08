t = int(input())
while(t):
    n,x = map(int, input().split())
    station = list(map(int,input().split()))
    diff = []
    
    for i in range(1,n,1):
        diff.append(station[i] - station[i-1])
    diff.append(2*(x-station[n-1]))
    diff.append(station[0])
    print(max(diff))
    t=t-1