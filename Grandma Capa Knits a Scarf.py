def fun_palindrom(s,l,r,remove):
    left = l
    right = r
    erased = 0
    n = len(s)

    while right< n and left<=right:
        if s[left]!=s[right]:
            if s[left]==remove:
                erased+=1
                left+=1
            elif s[right]==remove:
                erased+=1
                right-=1
            else:
                return -1
        else:
            left+=1
            right-=1
    return erased

def ans():
    n = int(input())
    s = input()
    
    l=r=-1
    for i in range(n//2):
        if s[i]!=s[n-1-i]:
            l=i
            r=n-1-i
            break
    if l==r:
        print('0')
        return
    # we can remove either s[i] or s[n-1-i]
    e1 = fun_palindrom(s,l,r,s[l])
    e2 = fun_palindrom(s,l,r,s[r])

    if e1==-1:
        print(e2)
    elif e2==-1:
        print(e1)
    else:print(min(e1,e2))

t = int(input())
while t:
    ans()
    t-=1