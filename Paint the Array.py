def gcd_(a,b): # assume b is small
    if b==0:
        return a
    return gcd_(b,a%b)
t= int(input())

while t:
    n = int(input())
    a = list(map(int,input().split()))
    beautiful = True
    d_even=a[0]

    for i in range(2,n,2):
        d_even=gcd_(a[i],d_even)

    for i in range(1,n,2):
        if a[i]%d_even==0:
            beautiful=False
            break

    if beautiful: print(d_even)

    if beautiful is False:
        beautiful = True
        d_odd = a[1]

        for i in range(3,n,2):
          d_odd=gcd_(a[i],d_odd)
        
        for i in range(0,n,2):
          if a[i]%d_odd==0:
            beautiful=False
            break
         
        print(d_odd) if beautiful else print('0')
    
    t-=1