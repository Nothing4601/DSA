t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    remove = 0
    i=0
    while i<n-1:

        if a[i]==a[i+1]:
            remove+=1
            i+=1

        elif a[i]>a[i+1]:

            i+=1

            while i<n-1 and a[i]>=a[i+1]:
                remove+=1
                i+=1

        elif a[i]<a[i+1]:

            i+=1

            while i<n-1 and a[i]<=a[i+1]:
                 remove+=1
                 i+=1
        else: i+=1
    print(n - remove)

    t-=1