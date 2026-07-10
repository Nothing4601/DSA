# what if i prestore inforemation for each index where is the nearest different elemetnt on right side store it index and not then -1
# then for each query l,r check sotred value at l and if store[l]<= r then print l and a[l] else -1 -1 

t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    
    near_diff = [-1]*n
    for i in range(n-1,0,-1):
         if a[i]==a[i-1]:
             near_diff[i-1] = near_diff[i]
         else:
             near_diff[i-1] = i+1
    print(near_diff)

    for i in range(q):
        l,r = map(int,input().split())
        if near_diff[l-1]>r or near_diff[l-1]==-1:
            print(-1,-1)
        else: # near differnece for given index is less than or equl to r
            print(l,near_diff[l-1])
        
    t-=1