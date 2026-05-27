# Queue Data Structure :
# A linear data structure that follows the FIFO (First In, First Out) principle.
# Insertion (enqueue) is performed at the rear/end of the queue.
# Deletion (dequeue) is performed from the front/start of the queue.
# Elements in the middle cannot be directly accessed or modified in a standard queue.
# Common uses:
# - Ticket booking systems
# - CPU task scheduling
# - Printer task management
# - Call center/customer service systems
# Used wherever the First-Come, First-Served (FCFS) rule is followed.

# WE CAN IMPLEMENT QUEUE USING: 1)Array
#                               2)Linked list
#                               3)Dequeue

#using Array 
class Queue_Array:
    def __init__(self):
        self.queue = []
    
    def q_add(self,value):
        self.queue.append(value)
    
    def q_isempty(self):
        return len(self.queue) == 0 

    def q_pop(self):
        if self.q_isempty():
            print('Queue is empty')
        else:
          print(f'{self.queue[0]} is deleted')
          self.queue.pop(0) # always delete first element as FIFO

# Using Linked List 
# below code use function form LinkedList/Singly_LL.py file
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from LinkedList.Singly_LL import Node,linkedlist
class Queue_LL:
    def __init__(self):
        self.queue = linkedlist()
    
    def q_add_LL(self,value):
        self.queue.LL_add(value)
    
    def q_isempty_LL(self):
        return self.queue.first_LLelement() is None
    
    def q_pop_LL(self): # pop first element
        if self.q_isempty_LL():
            print("Queue is Empty")
        else:
            print(f'{self.queue.first_LLelement()} is deleted')
            self.queue.LL_delete(self.queue.first_LLelement()) # first element delete
        
    
a=Queue_Array()
a.q_pop()
a.q_add(0)
a.q_add(10)
a.q_add(20)
a.q_add(40)
a.q_add(80)
a.q_add(160)
a.q_pop() # 0 is deleted
a.q_pop() # 10 is deleted
a.q_pop() # 20 is deleted
a.q_add(-15)
a.q_pop() # 40 is deleted

print('Now use Queue with LL...')

a=Queue_LL()
a.q_pop_LL()
a.q_add_LL(0)
a.q_add_LL(10)
a.q_add_LL(20)
a.q_add_LL(40)
a.q_add_LL(80)
a.q_add_LL(160)
a.q_pop_LL() # 0 is deleted
a.q_pop_LL() # 10 is deleted
a.q_pop_LL() # 20 is deleted
a.q_add_LL(-15)
a.q_pop_LL() # 40 is deleted
    