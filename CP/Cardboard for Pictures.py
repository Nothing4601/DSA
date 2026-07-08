
t = int(input())
while t:
    n,c = map(int, input().split())
    s = list(map(int,input().split()))
    low =1
    high = 10**9
    
    while(low<=high):
        mid = (low + high)//2
        sum_ = 0
        for i in s:
            sum_ += (i+2*mid)**2

        if sum_ < c:
            low = mid +1
        elif sum_ >c :
            high = mid - 1
        else:
           print(mid)
           break
    t-=1