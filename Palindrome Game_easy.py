t = int(input())
while t:
    n = int(input())
    s = input()
    count_zero = 0

    for i in range(n//2):
        if s[i]=='0':
           count_zero+=2
    
    if n%2 != 0 and s[n//2]=='0':
        count_zero+=1
    
    if count_zero%2==0:
        print('BOB')
    elif count_zero==1:
        print('BOB')
    else:
        print('ALICE')

    t-=1