# Find the maximum sum among all contiguous subarrays of fixed size k.
# Approach:
# 1. Compute the sum of the first k elements and store it as max_sum.
# 2. Check every subarray of size k:
#       nums[1 : k+1]
#       nums[2 : k+2]
#       ...
#       nums[n-k : n]
# 3.Keep track of maximum sum
# Time Complexity: O(n * k)

# Optimized Approch:
# Compute the first window sum of size k.
# For each next window, subtract the outgoing element
# and add the incoming element to get the new window sum.
# Keep track of the maximum window sum.
#
# Time Complexity: O(n)

import time
def max_subarray_sum_size(nums, k): # numbs--> array of number, k -> fixed size
    n= len(nums)
    max_sum = sum(nums[:k])
    for i in range(1,n-k+1,1):

        if max_sum < sum(nums[i:i+k]):
            max_sum=sum(nums[i:i+k])

    return max_sum

def max_subaaray_sum_size_optimize(nums, k):
    n=len(nums)
    curr_sum=max_sum=sum(nums[:k])
    
    for i in range(0,n-k,1):
        curr_sum = curr_sum - nums[i] + nums[i+k]

        if curr_sum > max_sum:
            max_sum = curr_sum
    
    return max_sum

print( max_subarray_sum_size([0,3,-6,9,-12,15,-18,21,-24,27,-30,33,-36,39,-42,45,-48,51,-54,57,-60],5) )

print( max_subaaray_sum_size_optimize([0,3,-6,9,-12,15,-18,21,-24,27,-30,33,-36,39,-42,45,-48,51,-54,57,-60],5) )
