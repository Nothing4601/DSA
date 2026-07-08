t = int(input())
while t:
    n= int(input())
    a = list(map(int,input().split()))
    diff_pos = []

    for i in range(n):
        if a[i]!=i:
            diff_pos.append(a[i])

    ans = diff_pos[0]

    for i in diff_pos:
          ans = ans & i
          
    print(ans)
    t-=1