a,b,c,d = map(int,input().split())

if a==b==c==d:
    ans=3
elif (a==b==c) or (a==b==d) or (b==c==d):
    ans=2
elif (a==b) or (a==c) or (a==d) or (b==c) or (b==d) or (c==d):
    if (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
        ans = 2
    else:
        ans=1
else:
    ans = 0
print(ans)