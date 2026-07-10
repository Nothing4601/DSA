def fun():
    n = int(input())
    a = list(map(int,input().split()))
             
    a_max = max(a)
    a_min = min(a)

    if a[0]== a_min or a[-1]==a_max:
        print(a_max-a_min)
        return 
    
    ans = max(a_max - a[0],a[-1] - a_min)
    for i in range(n-1):
        
        if (a[i]-a[i+1]) > ans:
            ans= a[i]- a[i+1]

    print(ans) 

t = int(input())
while t:
    fun()     
    t-=1