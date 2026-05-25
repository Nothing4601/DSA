# stack is Linear Data structure that works on LIFO(Last in First out) Principal: Like container with close base and top is open
# we can not access in between element like array or list
# Stack has both Fixed and Dynamic memory (Array and Linked list)
# three function :
    #  i) Push : add element at top
    #  ii) Pop : delete last element
    #  iii) Peek : Print top elementuse

class Stack:
    def __init__(self):
        self.container = []

    def push(self,value):
        self.container.append(value) # add value at last

    def pop(self) :
        if self.container:
          self.container.pop() # remove last element
        else:
          print("Stack is empty")

    def length(self):
        return len(self.container) # print() will just print on screen, return None
    
    def peek(self):
        if self.container:
          print(self.container[-1]) 
#      or print(self.container[ self.length() ])
        else:
            print('Stack is empty')

a= Stack()
print(a.length()) #0
a.pop()   # Stack is empty
a.peek()  #Stack is empty
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.peek() #4
a.pop()  
a.peek() # 3
a.pop()
print(a.length()) #2
a.peek() # 2
a.pop()
a.pop()
a.pop()
