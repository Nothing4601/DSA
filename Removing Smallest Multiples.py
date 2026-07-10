t = int(input())
while t:

    n = int(input())
    binary_str = input()
    cost = 0
    is_removed = [False]*n

    for i in range(1,n+1,1):

        for j in range(i,n+1,i):
            
            if binary_str[j-1]=='0':
                if is_removed[j-1] == False:
                   cost += i
                   is_removed[j-1] = True
            else: break
            
    print(cost)
    t-=1