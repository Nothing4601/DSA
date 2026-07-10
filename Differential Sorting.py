def ans_():
     n =int(input())
     a = list(map(int,input().split()))
     a_sorted = True
    # if array is already sorted then return 0
     for i in range(n-1):
          if a[i+1] < a[i] :
               a_sorted=False
               break
     ans = []
     if a_sorted:
          print(0)
          return 
     if a[-1]< 0 or a[-1] < a[-2]:
          print(-1)
          return 
     
    
     for i in range(n-2,0,-1):
    
          if a[i-1] > a[i]:
               ans.append([i,i+1,n])
               a[i-1] = a[i] - a[n-1]
    
     print(len(ans))
     for i in range( len(ans)):
          print(ans[i][0],ans[i][1],ans[i][2])
               


t = int(input())
while t:
    ans_()
    t-=1