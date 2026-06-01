# Sliding Window:
# Compute the first window sum of size k.
# For each next window, subtract the outgoing element
# and add the incoming element to get the new window sum.
# Keep track of the maximum window sum.
#
# Time Complexity: O(n)

def max_subaaray_sum_size_optimize(nums, k):
    n=len(nums)
    curr_sum=max_sum=sum(nums[:k])
    
    for i in range(0,n-k,1):
        curr_sum = curr_sum - nums[i] + nums[i+k]

        if curr_sum > max_sum:
            max_sum = curr_sum
    
    return max_sum