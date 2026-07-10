s = input()
n = len(s)
a=[]
for i in s:
    a.append(i)

for i in range(n-1):
     if a[i]==a[i+1]:
          ascii = ord(a[i+1])
          if ascii==122:
               ascii=96
          a[i+1]=chr(ascii+1)
          if i+2<n and a[i+1]==a[i+2]:
              a[i+1] = chr(ord(a[i+1])+1 if ord(a[i+1])!=122 else 97)
     

for char in a:
    print(char,end= '')
