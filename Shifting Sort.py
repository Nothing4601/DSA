# first find min for each iteration then change index of only that segment of element which is O(n*O(n+n))
t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    
    ans = []
    for i in range(n):
        min_index= i

        for j in range(i+1,n,1):
            if a[j]<a[min_index]:
                min_index = j
        
        if min_index == i: continue
        ans.append([i+1, min_index+1, min_index - i])
        for k in range(min_index,i,-1):
            a[k-1],a[k] = a[k], a[k-1]
    
    print(len(ans))
    for l in ans:
        print(l[0], l[1], l[2])
    t-=1