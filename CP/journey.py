t = int(input())
while(t):
    n,a,b,c = map(int,input().split())
    total = a+b+c
    mod =n//total
    #ans=(n%(a+b+c))*3
    if mod*total == n:
        print(mod*3)
    else:
     if (mod*total+a)<n:
        if (mod*total+a+b)<n:
            print(mod*3 + 3)
        else:
            print(mod*3+2)
     else:
        print(mod*3+1)
    t=t-1