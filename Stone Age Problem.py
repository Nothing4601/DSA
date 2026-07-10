n,q  = map(int,input().split())
a = list(map(int,input().split()))
dict_ = [] # (val, last updated time)
total_sum = 0

for i in range(n):
     dict_.append([a[i],0])
     total_sum+= a[i]

global_val = 0
global_time = 0
curr_time = 1

for j in range(q):
    query  = list(map(int,input().split()))

    if query[0]==2:
         total_sum = query[1]*n
         global_val = query[1]
         global_time = curr_time

    else: # 1st type of query
         index = query[1] -1
         temp_val = query[2]
         temp_time = dict_[index][1]

         if global_time > temp_time:
              total_sum= total_sum+temp_val-global_val
              dict_[index][1] = curr_time
              dict_[index][0] = temp_val

         else: # global time is less than or equal to temp_time 
              total_sum = total_sum + temp_val - dict_[index][0]
              dict_[index][0]= temp_val
    curr_time += 1
    print(total_sum)
         
    