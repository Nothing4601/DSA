t = int(input())
while t:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    doll = 1
    i = 1
    pre_max_conti= 0 
    while i<n:
    
      if a[i]-a[i-1]==1:
         i+=1
         if i<n and a[i] == a[i-1] + 1:
            pre_max_conti = 0
         
      elif a[i]==a[i-1]:
         conti = 1
         i+=1

         while i<n and a[i]==a[i-1]:
            conti+=1
            i+=1
         doll += max(0,conti - pre_max_conti)
         pre_max_conti = conti

      else:
         doll+=1
         pre_max_conti = 0
         i+=1

    print(doll)    
   
    t-=1