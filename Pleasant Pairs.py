t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    ans  = 0

    for i in range(n):
        for multiple in range(1,2*n,1):
            if a[i]*multiple > 2*n:
                break

            index = a[i]*multiple - (i+1) - 1
            if index<n and  index > i and a[index] == multiple:
                ans+=1
    print(ans)
    t-=1

