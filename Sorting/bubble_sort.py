# Check element pairwise, if first number is larger swap their position, repeat for end of array 
def Bubble_sort(a):
    n =len(a)
    for i in range(n):
        for j in range(0,n-i-1,1):
            if a[j] > a[j+1]:
                # a[j] is at j+1
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
    return a

print(Bubble_sort([3,2,5,23,18,20,3,5,6]))
