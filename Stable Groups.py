n,k,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
counts = []

for i in range(0,n-1,1):
    diff = a[i+1] - a[i]
    if diff > x:
        counts.append( (diff-1)//x )

counts.sort()
m = len(counts)
curr_sum = 0
store = 0

for i in range(m):
     curr_sum+=counts[i]
     if curr_sum <= k:
         store= i+1
     else:
         store = i
         break
print(m+1-store)