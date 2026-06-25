t = int(input())

while(t):
    n=int(input())
    string = str(input())
    use_char = []
    ans = 0
    for i in range(len(string)):
        if string[i] in use_char:
            continue
        else:
            use_char.append(string[i])
            ans = ans+(n-i)
    print(ans)
    t=t-1