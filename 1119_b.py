n,h = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
ans = False
for i in  range(len(a)):
    sum = sum + a[i]
    if sum > 2*h:
      a=a[:i]
      break
#print(a)
for j in range(len(a)):
   if j!=0:
      a_new = a[:-j]  # drop last j element
   else :
      a_new = a
   a_sort = sorted(a_new,reverse=True)
   #print(a_sort)
   h_remain=h
   for k in range(0,len(a_sort),2):
      if k==0:
         h_remain = h
      else :
         h_remain = h_remain - a_sort[k-2]
         #print('h_remian',h_remain)
      if a_sort[k] <= h_remain:
         #print(k,len(a_sort))
         if k==(len(a_sort) -1) or k== (len(a_sort)) -2:
            #print('inside loop')
            ans = True
            break 
   if ans:  
     print(len(a_sort))
     break
