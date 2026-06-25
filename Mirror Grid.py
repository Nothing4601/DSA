def fun_count_1(a,b,c,d):
    return (int(a)+int(b)+int(c)+int(d)) # as number is either 0 or 1

t = int(input())
while t:
    n = int(input())
    grid = [input() for _ in range(n)]
    operation = 0
    
    for i in range(n):
        for j in range(n):

            count_1 = fun_count_1(grid[i][j], grid[j][n-1-i], grid[n-1-j][i], grid[n-1-i][n-1-j])
            if count_1 >=2:
                operation += 4 - count_1
                
            else:
                operation+= count_1
                
    print(operation//4)
    t-=1
