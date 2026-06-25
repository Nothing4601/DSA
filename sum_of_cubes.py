import math
t= int(input())
def sum_of_cubes_1():
    x=int(input())
    cbrt_x= int(math.cbrt(x))
    dict={}
    for i in range(1,cbrt_x + 1,1):
        dict[i*i*i] = i # key is i^3 and value is i

    for j in dict: # j is in dict as key so if (x-j) is also as key in dict then ans is yes
        if (x-j) in dict:
            print('Yes')
            return
    print('No')
def sum_of_cubes_2():
    x=int(input())
    cbrt_x= int(math.cbrt(x))
    lower = 1
    higher = cbrt_x
    while(lower<=higher):
        if (lower**3 + higher**3)==x:
            print('Yes')
            return
        else:
            if (lower**3 + higher**3) <x:
                lower = lower+1
            else:
                higher= higher-1
    print('No')
    return
while(t):
    sum_of_cubes_2()
    t=t-1