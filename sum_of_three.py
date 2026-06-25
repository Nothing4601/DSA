t = int(input())
while(t):
    n = int(input())
    if n in [1,2,3,4,5,6,9]:
        print('NO')
    elif n==8:
        print('YES')
        print('2 5 1')
    else:
        print('YES')
        if(n%3==0):
            print(n-5,' 1',' 4')
        if(n%3==1):
            print(n-3,' 2',' 1')
        if(n%3==2):
            print(n-6,' 4',' 2')
    t=t-1