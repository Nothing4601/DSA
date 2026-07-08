t = int(input())
while t:
   a ,b = map(int,input().split())
   xk,yk = map(int, input().split())
   xq,yq = map(int, input().split())
   ans = 0
   king = [[xk-a,yk-b],[xk+a,yk+b],[xk-b,yk-a],[xk+b,yk+a],[xk-a,yk+b],[xk+a,yk-b],[xk-b,yk+a],[xk+b,yk-a]]
   queen = [[xq-a,yq-b],[xq+a,yq+b],[xq-b,yq-a],[xq+b,yq+a],[xq-a,yq+b],[xq+a,yq-b],[xq-b,yq+a],[xq+b,yq-a]]
   king_set = set(tuple(k) for k in king)
   queen_Set = set(tuple(q) for q in queen)
   
   for i in king_set:
      for j in queen_Set:
         if i==j:
            ans+=1
   print(ans)
   t-=1