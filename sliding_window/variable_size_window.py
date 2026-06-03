# find indicies of subaaray whose sum is equal to target sum given array has all positive integer including zero
# Since all elements are non-negative, we can maintain a window [start, end].
# - If window_sum < target, expand the window by moving end forward.
# - If window_sum > target, shrink the window by moving start forward.
# - If window_sum == target, return the window indices.
#
# Time Complexity: O(2*n) --> O(n)

def find_subarray_sum(a, target): # a is array of numbers
   start=end=0
   while(start<=end and end<len(a)): 
     window_sum = sum(a[start:end+1])
     if (window_sum==target): # more time complexity as compute sum in each time 
        print(start,':',end)
        return
     elif (window_sum < target):
         end+=1
     else:
         start+=1

# more optimized--> do not compute sum at each step
def find_subarray_sum_2(a,target):
   start = 0
   window_sum=0
   for end in range(len(a)):
      window_sum +=a[end]

      while window_sum>target:
        window_sum-=a[start]
        start+=1

      if window_sum==target:
        print(start,':',end)
        return

find_subarray_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) # -> (0,4)
find_subarray_sum([3, 1, 4, 9, 2, 1, 7], 10) # -> (4,6)

find_subarray_sum_2([3, 1, 4, 9, 2, 1, 7], 11) # -> (3,4)
find_subarray_sum_2([1, 2, 3, 7, 5], 12) # -> (1,3)

