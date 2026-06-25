t= int(input())
while(t):
    n = int(input())
    N = list(map(int, input().split()))
    N_sorted = sorted(N)
    score = 0
    dict_ ={}
    prefix_sum = []
    sum =0
    for j in range(n):
        sum =sum + N_sorted[j]
        prefix_sum.append(sum)

    for i in range(n):
        ans =i
        j=i
        while (j<n-1) and (prefix_sum[j] >= N_sorted[j+1]):
            ans+=1
            j+=1
        dict_[N_sorted[i]] = ans
    for num in N:
        print(dict_[num],end=' ')
    print('\n')
    t-=1