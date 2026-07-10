# for each element store it's remainder when divide with x and y in key of dict and value of dict if fre of this pair
# then find reqired remaider such that condi satisfy (remainder with y is same and sum of x remider is divisble with x) and then find frequency of required pair
# and add remiander of number pair to the dict

t = int(input())
while t:
    n , x, y = map(int,input().split())
    a = list(map(int,input().split()))
    
    freq = {}
    ans = 0
    for num in a:
        
        req_pair = (0 if num%x==0 else x-num%x ,num%y)
        count = freq.get(req_pair,0)
        ans+=count
        freq[(num%x , num%y)] = freq.get((num%x , num%y),0) + 1

    print(ans)
    t-=1