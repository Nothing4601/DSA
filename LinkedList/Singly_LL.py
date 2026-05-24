class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self,data):
        self.n1 = Node(data)
        
    def LL_add(self,value):
        if self.n1 is None:
            self.n1 = Node(value)
        else:
            temp = self.n1
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(value)

    def LL_delete(self, value):
        if self.n1 == None:
            print('No element in Linked List to delete')
        elif (self.n1.data==value):
            self.n1=self.n1.next
        else:
            temp = self.n1
            while(temp.next!=None and temp.next.data != value ):
                temp=temp.next
            if temp.next is not None:
               temp.next = temp.next.next
            else:
                print(f'{value} is not in the list')
    def LL_print(self):
        if self.n1 == None:
           print('Linked List is empty')
        else:
            temp = self.n1
            while(temp.next is not None):
                print(temp.data,end='-->')
                temp = temp.next
            print(temp.data)
    
a = linkedlist(50)
a.LL_add(10)
a.LL_add(20)
a.LL_add(30)
a.LL_add(40)
a.LL_add(60)
a.LL_print()
a.LL_delete(80)
a.LL_print()
        