t = int(input())
while t:
    n = int(input())
    b =list(map(int,input().split()))
    a = []
    a.append(b[0])

    for i in range(n-2):
        if b[i+1] < b[i]:
            a.append(b[i+1])
        else:
            a.append(b[i])
    a.append(b[-1])

    for num in a:
        print(num, end = ' ')
    print()
    t-=1