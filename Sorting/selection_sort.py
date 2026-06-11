# Selection Sort
# Find the minimum element in the unsorted part of the array.
# Swap it with the first element of the unsorted part.
# Repeat this process until the entire array is sorted.

# Time Complexity: O(n²)
# Space Complexity: O(1)

def Selection_sort(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i+1,n,1):
            if a[j] < a[min_index]:
                min_index = j
        temp = a[i]   
        a[i] = a[min_index]
        a[min_index] = temp

    return a
print(Selection_sort([3,2,5,23,18,20,3,5,6]))