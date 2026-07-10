def ans_():
     n = int(input())
     s = input()
     pos = {}
     for i in range(n):
          pos[97+i] = []
     for i in range(n):
          pos[ord(s[i])].append(i)
     
     # len 1 check
     for ascii in range(97, 97+26,1):
          if pos[ascii]== None:
               print(chr( ascii )) # convert number to it's charecter
               return
    
    # len 2 check
    
     print(pos)
          


t = int(input())
while t:
    ans_()
    t-=1