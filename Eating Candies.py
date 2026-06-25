t = int(input())
while t:
    n= int(input())
    w = list(map(int,input().split()))
    alice =0
    bob = n-1
    alice_sum = w[alice]
    bob_sum = w[bob]
    ans = 0

    while alice< bob and bob<n:
        
        if alice_sum > bob_sum:
            bob-=1
            bob_sum+=w[bob]

        elif alice_sum==bob_sum:
            ans = alice + 1 + (n-bob)
            alice+=1
            alice_sum += w[alice]
        else:#alice_sum < bob_sum
            alice+=1
            alice_sum += w[alice]
    print(ans)
    t-=1