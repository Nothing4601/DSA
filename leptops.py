def Leptops(): 
 n = int(input())
 d= {}
 for _ in range(n):
    a,b = map(int,input().split())
    d[a] = b
 sort_dict = dict(sorted(d.items()))
 
 pre_key = None
 for key in sort_dict:
   if pre_key is not None:
     if (key - pre_key)*(sort_dict[key] - sort_dict[pre_key])<0:
       print('Happy Alex')
       return
   pre_key=key
 print('Poor Alex')
     
Leptops()

#     A.append(a)
#     B.append(b)
#  for i in range(1,n,1):
#     if (A[i] - A[i-1])*(B[i] - B[i-1]) <0:
#         print('Happy Alex')
#         return
#  print('Poor Alex')
 