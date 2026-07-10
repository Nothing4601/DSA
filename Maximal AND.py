t = int(input())
while t:
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    
    operation_count = [0]*31 # 0 to 30 bit

    for num in a:
        binary_string = f"{num:031b}"

        for i in range(31):
            if binary_string[i]=='0':
                operation_count[i]+=1
        
    ans = 0
    for i in range(31):
        if operation_count[i]<= k:
            ans+= 2**(30-i)
            k-=operation_count[i]
    
    print(ans)
    
    t-=1
