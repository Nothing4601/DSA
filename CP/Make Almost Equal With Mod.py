def check_same_mod(power,a):
    num = 2**power
    return all(i%num ==a[0]%num for i in a)

t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    
    power_of_2 = 1
    while check_same_mod(power_of_2,a):
        power_of_2+=1
    
    print(2**power_of_2)

    t-=1