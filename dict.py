dict = {}
dict['a'] = 1
dict['b'] = 2
dict[1] = 'aa'
for x in dict:
    print(x)

print('b :',dict['b'])
print('1 :',dict[1])
#print('2 :',dict[2]) # keyerror 2 
 

dict1 = []
dict1['a'] = 1
print(dict1) # list indices must be integers or slices, not str