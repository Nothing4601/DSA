# Find the maximum sum among all contiguous subarrays of fixed size k.
# Approach:
# 1. Compute the sum of the first k elements and store it as max_sum.
# 2. Check every subarray of size k:
#       nums[1 : k+1]
#       nums[2 : k+2]
#       ...
#       nums[n-k : n]
# 3. If the current subarray sum is greater than max_sum,
#    update max_sum.
#
# Time Complexity: O(n * k)

def max_subarray_sum_size(nums, k): # numbs--> array of number, k -> fixed size
    n= len(nums)
    max_sum = sum(nums[:k])
    for i in range(1,n-k+1,1):

        if max_sum < sum(nums[i:i+k]):
            max_sum=sum(nums[i:i+k])
            
    return max_sum