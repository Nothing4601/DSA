def ans_():
    n = int(input())
    a = input()
    b = input()
    pref = []
    pref.append([1,0]) if a[0]=='0' else pref.append([0,1])
    
    # count pref 0s and 1s
    for i in range(1,n,1):
        if a[i]=='0':
            pref.append([ pref[i-1][0] + 1, pref[i-1][1] ])
        else:
            pref.append([ pref[i-1][0], pref[i-1][1] + 1 ])
    
    operation = 0
    for i in range(n-1,-1,-1):
        if operation%2==0: # a is not change
            if a[i] != b[i]:
                 if pref[i][0]==pref[i][1]: # check pref 0 and 1 are same ?
                     operation+=1
                 else:
                     print('NO')
                     return
        else: # a change , 0-->1 and 1-->0
             if a[i]==b[i]:
                  if pref[i][0]==pref[i][1]:
                       operation+=1
                  else:
                      print('NO')
                      return
    print('YES') 

    
t = int(input())
while t:
    ans_()
    t-=1