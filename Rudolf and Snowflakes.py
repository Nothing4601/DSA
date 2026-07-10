check = []
max_n = 10**6
max_k = 10**3
min_k = 2

for i in range(min_k,max_k,1): # mqx_n never reach so max_k - 1 
     curr_sum = i*(i+1) + 1
     if curr_sum> max_n:
          break
     
     check.append(curr_sum)
     power = 3
     while curr_sum + i**power < max_n:
          curr_sum += i**power
          check.append(curr_sum)
          power+=1
check.sort()
m = len(check)

t = int(input())
while t:
    n = int(input())
    l=0
    r= m-1
    loop_break = False

    while l<=r:
         
         mid = l + (r-l)//2

         if check[mid]==n:
              print('Yes')
              loop_break = True
              break
         
         elif check[mid] < n:
              l = mid +1

         else:
              r=mid-1
              
    if loop_break == False:
         print('No')
         
    t-=1