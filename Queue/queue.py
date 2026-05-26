# Liner data structure which use FIFO
# use : ticket booking, or CPU task scheduling, where first-come first-served rule is followed.
# only add element at last and delete element from the start cant access middle element
class Queue:
    def __init__(self):
        self.queue = []
    
    def q_add(self,value):
        self.queue.append(value)
    
    def q_is_empty(self):
        return len(self.queue) == 0 

    def q_pop(self):
        if self.q_is_empty():
            print('Queue is empty')
        else:
          print(f'{self.queue[0]} is deleted')
          self.queue.pop(0) # always delete first element as FIFO
    
a=Queue()
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
a.q_is_empty()

    