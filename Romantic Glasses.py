# difference of odd and even sum is zero
# make one array consisting of even and odd sum of all prefix
# then any subarray is exit whose sum is zero if in new prefix array any element is repeat
import sys
input = sys.stdin.readline
def ans_():
    n = int(input())
    a = list(map(int,input().split()))
    
    pref = []
    pref.append(a[0])
    
    for i in  range(1,n,1):
    
        if i%2==0:
            pref.append(pref[i-1]+a[i])
        else:
            pref.append(pref[i-1]-a[i])

        if pref[i]==0:
            print('Yes')
            return
    
    seen = set()

    for x in pref:
        if x in seen:
            print('Yes')
            return
        seen.add(x)
        
    print("No")   


t = int(input())
while t:
    ans_()
    t-=1