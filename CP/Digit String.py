# first count maximum string length that can be beafutiful then substract it from len(s)
def digit_string_1(): 
 t = int(input())
 while(t):
    s = input()
    prefix_2 = 0
    suffix_1_3 = 0
    fours=0
    n =len(s)
    for i in range(len(s)):
        if s[i]=='4':
            fours+=1
        if s[i] =='2':
            prefix_2+=1
    # number is such that all 2's are left of 1's and 3's
    suffix_1_3 = len(s) - prefix_2-fours
    ans= suffix_1_3
    prefix_2=0
    for j in range(len(s)): # only 1,2 or 3 present in s
        if s[j]=='2':
            prefix_2+=1
        if s[j]=='1' or s[j]=='3':
            suffix_1_3-=1
        ans = max(ans,prefix_2+suffix_1_3)
    print(n - ans)
    t-=1

# directly find minimum element that is being removed
def digit_string_2():
    t= int(input())
    while(t):
        s = input()
        n=len(s)
        fours=0
        suffix_2=0
        pre_1_3 = 0
        ans=0
        for i in s:
            if i=='4':
                fours+=1
            if i=='2':
                suffix_2 += 1
        ans = fours + suffix_2
        for i in s:
            if i=='2':
                suffix_2-=1
            if i=='1' or i=='3':
                pre_1_3 +=1
            ans = min(ans,pre_1_3 + suffix_2+fours)
        print(ans)
        t-=1

digit_string_2()