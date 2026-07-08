t = int(input())
def check_parity(a,b):
     return (a%2 ==b%2)

while t:
    n  =int(input())
    nums = list(map(int, input().split()))
    max_ = -1000
    curr_sum=0
    for i in range(n):
        curr_sum+=nums[i]
        max_ = max(curr_sum,max_)
        if curr_sum<0 or (i!= n-1 and check_parity(nums[i],nums[i+1])):
            curr_sum=0
    print(max_)
    t-=1