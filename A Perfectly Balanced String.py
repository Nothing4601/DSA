def fun_():
    s = input()
    n = len(s)
    used_char =[]
    repeat_char = False
    k=0
    for i in range(n):
        if s[i] not in used_char:
            used_char.append(s[i])
            k+=1
        else:break

    for j in range(0,n-k,1):
        if s[j]!= s[j+k]:
            repeat_char=True
            break

    if repeat_char:print('No')
    else: print('Yes')
t = int(input())
while t:
    fun_()
    t-=1
