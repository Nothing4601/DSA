t= int(input())
while t:
   n, k =map(int,input().split())
   a = list(map(int,input().split()))
   a.sort()
   #ai-aj=k if such ai and j exist in list a then ans is YES
   i=1
   j=0
   ans = False
   while j<n-1 and i<n:
      if a[i] -a[j] > k:
         j+=1
      elif (a[i] - a[j]) == k:
         ans =True
         break
      else:# a[i] - a[j] < k
         i+=1
   print('Yes') if ans else print('No')
   t-=1