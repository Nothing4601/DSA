# so any score have las m element for any sequence as this are the maximum element
# so check using binary search that (mid element/length) is equl or greater than 1 if yes then chek on left side else right side
t = int(input())
while t:
    n = int(input())
    a= list(map(int,input().split()))
    
    print(1,end=' ')
    for i in range(1,n,1):
        l=0
        r=i
        length = i+1
        ans = 1
        while l<=r:
            mid = l + (r-l)//2
            if a[mid]/(length-mid) >=1:
                r=mid-1
                ans  = length - mid
            else : l=mid + 1
        
        print(ans,end= ' ')
    print()
            
                 
        

        
    print()
    t-=1