t = int(input())
while t:
    n,k,a,b= map(int,input().split())
    x=[]
    y=[]
    
    for i in range(n):
        xx , yy = map(int, input().split())
        x.append(xx)
        y.append(yy)

    ans = abs(x[a-1] - x[b-1]) + abs(y[a-1] - y[b-1]) # if less than 2 major city 

    da = 10**10
    db = 10**10
    
    for j in range(k): # all major cities
         da = min(da,abs(x[a-1]-x[j]) + abs(y[a-1] - y[j]))
         db = min(db,abs(x[b-1]-x[j]) + abs(y[b-1] - y[j]))
    ans = min(ans , da+db)
    print(ans)
    t-=1