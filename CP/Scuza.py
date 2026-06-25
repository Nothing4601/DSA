t = int(input())
while t:
    n,q = map(int,input().split())
    steps = list(map(int,input().split()))
    legs = list(map(int,input().split()))
    ans = [0]*q
    a =[]

    for i in range(q):
        a.append((i,legs[i]))
    
    a.sort(key = lambda x: x[1])

    i=0
    curr_jump = 0
    j=0
    
    curr_ans = 0
    while i<q:
         while j<n and a[i][1]>=steps[j]: #a[i][1] --> value at index i in sorted array
             
             curr_ans += steps[j]
             j+=1

         original_index = a[i][0]
         ans[original_index] = curr_ans
         i+=1

    for num in ans:
        print(num, end =' ')
    print()

    t-=1