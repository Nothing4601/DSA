def binary_dequeue():
    n,s = map(int,input().split())
    a = list(map(int,input().split()))

    curr_sum = a[0]
    total_sum = sum(a)
    r=l=0
    length = 0

    if total_sum < s:
        print('-1')
        return
    if total_sum ==s:
        print('0')
        return
    
    while r<n and l<=r:
       
       if curr_sum == s:
           length = max(length,r-l+1)
           r+=1
           if r<n:
              curr_sum+=a[r]
       elif curr_sum< s:
           r+=1
           if r<n:
             curr_sum+= a[r]
       else:
           curr_sum-= a[l]
           l+=1

    print(n - length)



t =int(input())
while t:
    binary_dequeue()
    t-=1