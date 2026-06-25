import statistics
def fun():
    n,m,l = map(int,input().split())
    matrix = []
    for _ in range(n):
      matrix.extend(map(int,input().split()))

    for i in matrix:
       if i%l == matrix[0]%l:
          continue
       else :
         print('-1')
         return
    for i in range(len(matrix)):
        matrix[i]=matrix[i]//l
    med =statistics.median(matrix)

    ans = sum(abs(j-med) for j in matrix)
    print(int(ans))
fun()