t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    a1 = list(map(int,input().split())) 
    
    start=-1
    end=0

    for i in range(n):
        if a[i] != a1[i]:
            if start==-1:
              start=i
            else:
              end =i

    a1_min = min(a1[start:end+1])
    a1_max = max(a1[start:end+1])
    

    while 1<=start and a1_min>=a1[start-1]:
         start-=1
         a1_min = a1[start]
    
    while end<=n-2 and a1_max<=a1[end+1]:
         end+=1
         a1_max = a1[end]
    print(start +1,end+1)
    t-=1