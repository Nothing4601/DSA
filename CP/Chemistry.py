t = int(input())
while t:
    n,k = map(int,input().split())
    s = input()
    char_freq = {}

    for i in range(n):
        char_freq[s[i]]=char_freq.get(s[i],0) + 1
        
    even = 0
    odd = 0
    
    for i in char_freq:
        if char_freq[i]%2 ==0:
            even+=1
        else:odd+=1
    if (n-k)%2 ==0: 
        if (k-odd)>=0 and (k-odd)%2==0:
            print('Yes')
        else: print('No')
    else:# n-k is odd
        if (k-odd+1)>=0 and (k-odd+1)%2 == 0:
            print('Yes')
        else: print('No')
    t-=1