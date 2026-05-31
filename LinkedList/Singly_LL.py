class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_LL(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(value)

    def delete_LL(self, value):
        if self.head == None:
            print('No element in Linked List to delete')
        elif (self.head.data==value):
            self.head=self.head.next
        else:
            temp = self.head
            while(temp.next!=None and temp.next.data != value ): # check temp.next is not none --> happens when value is not in the lsit
                temp=temp.next
            if temp.next is not None:
               temp.next = temp.next.next
            else:
                print(f'{value} is not in the list')

    def print_LL(self):
        if self.head == None:
           print('Linked List is empty')
        else:
            temp = self.head
            while(temp.next is not None):
                print(temp.data,end='-->')
                temp = temp.next
            print(temp.data)
    
    def  firstelement_LL(self): # this fun used in Queue implementation usinf LinkedLIst
        if self.head:
            return self.head.data
        else:
            return None
if __name__ == "__main__":   
 a = LinkedList()
 a.add_LL(50)
 a.add_LL(10)
 a.add_LL(20)
 a.add_LL(30)
 a.add_LL(40)
 a.add_LL(60)
 a.print_LL()
 a.delete_LL(80)
 a.print_LL()
 a.delete_LL(30)
 a.delete_LL(60)
 a.delete_LL(20)
 a.delete_LL(50)
 a.print_LL()