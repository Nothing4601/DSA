# Deque (Double-Ended Queue) is more flexible:
#  Insertion can be done at both front and rear
#  Deletion can also be done from both front and rear

class dequeue:
    
    def __init__(self):
        self.dequeue = []
    
    def dq_add_rear(self,value):
        self.dequeue.append(value)
    
    def dq_isempty(self):
        return len(self.dequeue) == 0 

    def dq_pop_front(self):
        if self.dq_isempty():
            print('Dequeue is empty')
        else:
          print(f'{self.dequeue[0]} is deleted')
          self.dequeue.pop(0) 
        
    def dq_add_front(self,value):
        self.dequeue.insert(0,value)

    def dq_pop_rear(self):
        if self.dq_isempty():
            print('Dequeue is empty')
        else:
            print(f'{self.dequeue[-1]} is deleted')
            self.dequeue.pop()

a = dequeue()

a.dq_add_front(1)
a.dq_pop_rear() # 1 is deleted
a.dq_pop_front()# Dequeue is empty

a.dq_add_rear(20)
a.dq_add_rear(40)
a.dq_add_rear(80)
a.dq_add_rear(160)

a.dq_add_front(10)
a.dq_add_front(0)

a.dq_pop_rear() # 160 is deleted
a.dq_pop_rear() # 80 is deleted
a.dq_pop_front() # 0 is deleted
a.dq_pop_front() # 10 is deleted