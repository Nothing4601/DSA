# def gcd(a,b): # assume b is small
#     if b==0:
#         return a
#     else: return gcd(b,a%b)
from math import gcd
t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    freq_dict = {}

    for i in range(n):
        freq_dict[ a[i] ] = i+1

    ans = -1
    unique_num = [x for x in freq_dict]

    for i in range(len(unique_num)):

        for j in range(i,len(unique_num),1):

            if gcd(unique_num[i], unique_num[j]) == 1: # coprime
                ans = max(ans, freq_dict[ unique_num[i] ] + freq_dict[ unique_num[j] ])

    print(ans)
    t-=1