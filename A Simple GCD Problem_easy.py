def gcd_(a,b):
    if b==0:
        return a
    return gcd_(b,a%b)

def lcm_(a,b):
    return (a*b)/gcd_(a,b)

def fun_(x,y,z):
    return lcm_(gcd_(x,y), gcd_(y,z))


t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    operation = 0

    for i in range(1,n-1,1):
        if a[i] > fun_(a[i-1],a[i],a[i+1]):
            operation+=1

    if a[0] > gcd_(a[0],a[1]):
        operation+=1

    if a[-1] > gcd_(a[-1],a[-2]):
        operation+=1

    print(operation)
    t-=1