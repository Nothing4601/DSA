# n,t = map(int,input().split())
# a = list(map(int,input().split()))

# for i in range(1,n,1):
#     if sum(a[:i])>t:
#         diff=i
#         ans = i-1
        
# for x in range(1,n,1):
#     for y in range(x+diff, n+1, 1):
        
#         if sum(a[x:y])<t:
#             if y-x>ans:
#                 ans=y-x
#                 diff=ans+2
#             break
# print(ans)

n,t = map(int,input().split())
a = list(map(int,input().split()))

start =0
window_sum=0
ans=0
for end in range(n):
   window_sum += a[end]
   while window_sum > t:
      window_sum-=a[start]
      start+=1
   books=end-start+1
   ans=max(ans,books)
print(ans)