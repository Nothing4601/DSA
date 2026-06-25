def three_largest(a):  # just find three maximum index for each array
    index_3 = [-1]*3 # a_3 array store index
    n = len(a)
    for i in range(n):

        if index_3[0]==-1 or a[i]> a[index_3[0]] : # a_3[0] is first element which is index of max
            index_3[2] = index_3[1]
            index_3[1] = index_3[0]
            index_3[0] = i

        elif index_3[1]==-1 or a[i] > a[index_3[1]]: 
            index_3[2] = index_3[1]
            index_3[1] = i

        elif index_3[2]==-1 or a[i] > a[index_3[2]]: 
            index_3[2] = i

    return index_3

t = int(input())
while t:
    n = int(input())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ans = 0

    for i in three_largest(A):
         for j in three_largest(B):
              for k in three_largest(C):
                  if i!=j and i!=k and j!=k:
                       ans = max(ans, A[i] + B[j] + C[k])
    
    print(ans)
    t-=1