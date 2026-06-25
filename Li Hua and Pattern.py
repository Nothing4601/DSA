import copy
t = int(input())
while t:
    n, k = map(int,input().split())
    a = []
    a = [list(map(int,input().split())) for _ in range(n)]
    a_target = copy.deepcopy(a)
    # below for loop rotate the current pattern by 180 degree
    for i in range(n//2): # j loop through whole array 
        a_target[i],a_target[-1-i] = a_target[-1-i],a_target[i]

        for j in range(n//2): # k loop inside each row
            a_target[i][j],a_target[i][-1-j] = a_target[i][-1-j], a_target[i][j]
            
            a_target[-1-i][j],a_target[-1-i][-1-j] = a_target[-1-i][-1-j], a_target[-1-i][j]
    if n%2 !=0:
      for j in range(0,n//2,1):
           a_target[n//2][j], a_target[n//2][-1-j] = a_target[n//2][-1-j], a_target[n//2][j]
    
    k_min = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] != a_target[i][j]:
                k_min += 1
    k_min = k_min//2 # comparison happend two times     
    if k_min> k :
        print('No')
    elif n%2 != 0: # k_min is =< k
        print('Yes')
    else:
        if (k - k_min)%2 == 0:
            print("Yes")
        else : print('No')
    t-=1