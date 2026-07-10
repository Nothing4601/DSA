n = int(input())
m = [[ 0 for _ in range(n)] for _ in range(n)]

num = 1
for i in range(n):
    if i%2 == 0:
        for j in range(n):
            m[j][i] = num
            num += 1
    else:
        for j in range(n-1,-1,-1):
            m[j][i] = num
            num+=1

# print ans
for i in range(n):
    for j in range(n):
        print(m[i][j],end = ' ')
    print()