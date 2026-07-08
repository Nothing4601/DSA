a = str(input())
b = str(input())

# len(b) >= len(a)
def h_dist_sum_1(a,b): # time limit exceed for test case 9 
   count =0
   for i in range(len(b)-len(a) + 1): 
    sub_b = b[i:i+len(a)]
    for j in range(len(a)):
        
        if sub_b[j]!=a[j]:
            count+=1
   print(count)

def h_dist_sum_1(a,b):
   count =0
