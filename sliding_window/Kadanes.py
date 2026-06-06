# Kadane's Algorithm with Indices
# Keep a running sum of the current subarray.
# If the running sum becomes negative, start a new subarray from the next index.
# Whenever a larger sum is found, update the maximum sum and store
# the start and end indices of that subarray.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
import math
def max_subarray_sum(a): # a --> array of numbs
    # Array have both positive and negative element
    curr_sum = 0
    max_= -math.inf
    start_ind=end_ind =0
    for i in range(len(a)):
        # if my curr sum is zero mean we started new subarray
        if curr_sum==0:
            start = i

        curr_sum+=a[i]

        if curr_sum > max_:
          max_ = curr_sum
          start_ind = start
          end_ind = i

        if curr_sum<0:
            curr_sum=0
    print(f'{start_ind} : {end_ind}')

