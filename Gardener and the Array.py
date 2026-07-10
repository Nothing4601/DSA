# first make map which count number of particular bit 
# then for each number check if there exist a number such taht all of it's bists count is greater than 1 in all numbers then print YES, for one number all bits are unique

def ans_():
    n = int(input())
    bit_count = {}
    a=[]
    for i in range(n):
        a.append( list(map(int,input().split())) )

        for j in range(1,a[i][0]+1,1):
             bit_count[a[i][j]] = bit_count.get(a[i][j],0) + 1
    
    for i in range(n):
        loop_break = False

        for j in range(1,a[i][0]+1,1):

            if bit_count[ a[i][j] ] ==1:
                loop_break = True
                break
        if loop_break==False: # means all bit has count greter than 1 in all numbers
            print('Yes')
            return
    print('No')
    
t = int(input())
while t:
    ans_()
    t-=1