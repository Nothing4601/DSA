t= int(input())
while t:
    n = int(input())
    s = input()
    ans = 2 # string has atleast one element so default we need two unique number
    conti = 1
    for i in range(1,n,1):
        if s[i]==s[i-1]:
             conti+=1
             ans = max(ans,conti+1)
        else:
            conti=1
    print(ans)
    t-=1