# for ech number in array factorize it , then increse count of prime divisour in dict named 'exponent'

import math
def ans():
    n = int(input())
    a = list(map(int,input().split()))
    exponent = {}
    if n==1:
        print('Yes')
        return
    for i in range(n):
        x = 2
        num = a[i]
        while x*x<=num :
            if num%x==0:
                exponent[x] = exponent.get(x,0) + 1
                num = num//x
            else : 
                x+=1
        if num>1:
            exponent[num] = exponent.get(num,0) + 1

    for y in exponent:
       if exponent[y]%n!=0:
           print('No')
           return
    print("Yes")

t = int(input())
while t:
    ans()
    t-=1