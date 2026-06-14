# Insertion Sort
# Insert each element into its correct position in the
# already sorted left part of the array.
#
# Time Complexity: O(n²)
# Best Case: O(n) (already sorted)
# Space Complexity: O(1)
def Insertion_sort(a):
    n =len(a)
    for i in range(n):
        j=i
        while (j!=0 and a[j]<a[j-1]):
            a[j] , a[j-1] = a[j-1], a[j]
            j-=1
    return a
print(Insertion_sort([3,2,5,23,18,20,3,5,6]))