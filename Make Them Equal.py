def fun_():
    n, c = input().split()
    n= int(n)
    s = input()
    count_not_c = 0
    for i in range(n):
        if s[i]!=c:
           count_not_c+=1
    
    if count_not_c==0:
        print('0')
        return
    
    ans = True
    for i in range(1,n+1,1):
        if s[i-1]!=c:
            ans = False # means need 2 operation
            continue

        for j in range(i,n+1,i): # go into tthis for loop when s[i-1] is c
            if s[i-1]!=s[j-1]:
                ans = False
                break
            else: ans = True
        if ans:
            print(1)
            print(i)
            return
    print(2)
    print(n,n-1)  
t= int(input())
while t:
    
    fun_()
    t-=1
