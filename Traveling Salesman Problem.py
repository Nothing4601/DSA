t = int(input())
while t:
    n = int(input())
    ans = 0
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    for i in range(n):
        x,y = map(int,input().split())
        x_min = min(x_min,x)
        x_max= max(x_max,x)
        y_min = min(y_min,y)
        y_max = max(y_max,y)
    ans = 2*( abs(x_min) + x_max + y_max + abs(y_min) )
    print(ans)
    t-=1