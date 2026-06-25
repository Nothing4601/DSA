def gcd_(a,b):
    if b==0:
        return a
    return gcd_(b,a%b)

def lcm_(a,b):
    return (a*b)//(gcd_(a,b))

t= int(input())
while t:

    n,x,y = map(int,input().split())
    lcm_xy = lcm_(x,y)
    num_x = n//x - n//lcm_xy
    num_y = n//y - n//lcm_xy

    ans = (num_x*(2*n - num_x + 1))//2 - (num_y*(num_y+1))//2
    print(ans)

    t-=1