def fun_():
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    m = 0 # length of b

    for i in range(1,n+1,1):
        if a[i-1]<i:
            b.append([a[i-1],i])
            m+=1           
    #print('b',b)
    #binary search on prefix 
    ans = 0
    if m<2:
        print(ans)
        return
    for i in range(m-1,0,-1):
        curr_ans = 0
        l = 0
        r = i
        check = b[i][0]
        #print(f'value first element {b[i]}')
        while l<=r:
            mid = l + (r-l)//2
            if b[mid][1] < check:
                curr_ans = mid+1
                
                l=mid+1
            else:
                r=mid-1
        ans+=curr_ans
        #print(f'curr ans {curr_ans}, ans = {ans}')
    print(ans)

t = int(input())
while t:
    fun_()
    t-=1
