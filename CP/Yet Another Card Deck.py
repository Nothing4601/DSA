n,q = map(int,input().split())
colors = list(map(int,input().split()))
queries = list(map(int,input().split()))
dict_50 = {}

for i in range(n): # for colors array
   dict_50[ colors[i] ] = dict_50.get(colors[i],i+1)

for q in queries: # for queries array
    print(dict_50[ q ], end=' ') 
    for j in dict_50:
        if dict_50[j]<dict_50[q]:
            dict_50[j] += 1
        else: break
    dict_50[ q ] = 1