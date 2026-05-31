class Node:
    def __init__(self,data):
        self.data = data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

class Doubly_LinkedList:
    def __init__(self):
        self.head = None
    
    def add_DLL(self,value,x=None):
        '''value -> value to be inserted
           x     -> insert after node containing x
    
           If x is None, insert at beginning.'''
        if self.head is None:
            self.head = Node(value)
            
        elif x==None:
            # insert at starting
            temp = self.head

            self.head=Node(value)
            self.head.next = temp
            temp.prev=self.head
            
        else:
            temp = self.head
            while(temp.next!=None):
                if(temp.data==x):
                    temp2=Node(value)
                    
                    # Forward links
                    temp2.next=temp.next
                    temp.next=temp2

                    # Backward links
                    temp2.next.prev = temp2
                    temp2.prev= temp
                    return
                temp = temp.next
                
            if (temp.next is None):
               if (temp.data==x): 
                  temp2=Node(value)

                  temp.next=temp2
                  temp2.prev=temp
                  
               else:
                  print(f'Value {x} not found')
                
    def delete_DLL(self,value):
        if self.head == None : # LL is empty
            print('Linked List is empty')
        elif (self.head.data==value):  # Delete first element of LL
            self.head = self.head.next
            if self.head: # if new self.head is not None then also delete it's prev pointer
              self.head.prev=None
        else:
            temp = self.head
            while(temp.next!=None):
                if temp.data==value:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                    return
                temp=temp.next
            if temp.next is None:
                if temp.data==value: # Delete last element
                    temp.prev.next=None
                else:
                    print(f'Value {value} not found')
                 
    def print_DLL(self):
        if self.head is None:
            print('Linked List is empty')
            return
        temp=self.head
        #  Traverse from head to tail
        while (temp.next!=None):
            print(temp.data, end=' <--> ')
            temp=temp.next
        print(temp.data)

if __name__=="__main__":
 a=Doubly_LinkedList()
 a.delete_DLL(0)
 a.add_DLL(3)
 a.add_DLL(1)
 a.add_DLL(5,3)
 a.add_DLL(2,1)
 a.add_DLL(0)
 a.add_DLL(6,5)
 a.add_DLL(4,3)
 a.add_DLL(10,6)
 a.add_DLL(12,7)
 a.print_DLL()
 a.delete_DLL(0)
 a.delete_DLL(6)
 a.delete_DLL(2)
 a.delete_DLL(50)
 a.print_DLL()
