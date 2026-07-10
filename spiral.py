# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
m = [ [0 for _ in range(n)]  for _ in range(n)]

top = 0
bottom = n-1
right = n-1
left = 0
num = 1

while num <= n**2:
 for i in range(left,right + 1, 1):
     m[top][i] = num
     num+=1
 top+=1

 for i in range(top,bottom + 1, 1):
     m[i][right] = num
     num+=1
 right-=1

 for i in range(right,left - 1, -1):
     m[bottom][i] = num
     num+=1
 bottom-=1

 for i in range(bottom,top - 1, -1):
     m[i][left] = num
     num+=1
 left += 1
# ans
for i in range(n):
    for j in range(n):
        print(m[i][j], end = ' ')
    print()