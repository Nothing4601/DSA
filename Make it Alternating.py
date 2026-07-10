# first count contineous element, do not include 1, in 'conti' array
# then no of different shortest sequece is factorial of each number in contineous and then multiply all
# no of operation is sum of (each eleemnt of conti -1) 
t = int(input())
while t:
    s = input()
    n = len(s)
    operation = 0
    ans = 1
    mod = 998244353
    i=1
    while i<n:
        curr_conti = 1

        while i<n and s[i]==s[i-1]:
            curr_conti+=1
            i+=1
        operation += curr_conti-1
        ans*= curr_conti
        ans = ans%mod
        i+=1

    for j in range(operation,1,-1):
         ans *= j
         ans = ans % mod

    print(operation, ans)
    t-=1