t = int(input())
while t:
    s = input()
    ones = 0
    ans = 0
    for i in (s+s): # s+s --> check for cyclic ones
       if i=='1':
           ones+=1
           ans = max(ans,ones)
       else :
           ones = 0

    if ans//2 >= len(s):
        print(len(s)**2)
    else:
        print( ((ans+1)//2)*((ans+2)//2) )
    t-=1