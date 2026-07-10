def ans():
    n,k = map(int,input().split())
            
    if n%2==0:

        remainder = k%n
        if remainder==0: return n
        return remainder
    
    else: # n is odd
       steps = k-1 # as k represent hour at k=1 0 steps 
       extra_step = (k-1)//(n//2) # as every n//2 we take one extra step
       total_steps = steps + extra_step
       index = total_steps%n + 1 # +1 as we want 1 to n not from 0 to n-1
       return index

t = int(input())
while t:
    print(ans())
    t-=1