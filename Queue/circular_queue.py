# In a normal queue:
# - Insertion happens at the rear
# - Deletion happens from the front

# Problem in fixed-size linear queue:
# - Deleted front spaces cannot be reused
# - Rear keeps moving forward
# - This causes memory wastage

# Solution: Circular Queue
# - Last position connects back to the first position
# - Freed spaces are reused efficiently
# - Prevents memory wastage

class Circular_queue:
    def __init__(self,size):
        self.size=size
        self.cq=[None]*size
        self.front=self.rear=-1

    def cq_add(self,value): # at last
        if self.front==-1:
            self.front=self.rear=0
            self.cq[self.front] = value
        elif (self.rear+1)%self.size == self.front:
            print('Circular Queue is full')
        else:
            self.rear=(self.rear+1)%self.size
            self.cq[self.rear] = value
        
    def cq_delete(self):# from front
        if self.front==-1:
            print("Circular Queue is empty")
        elif self.front==self.rear: # means both are 0 
            print(f'{self.cq[self.front]} is deleted')
            self.front=self.rear=-1
        else:
           print(f'{self.cq[self.front]} is deleted')
           self.front = (self.front + 1)%self.size

a = Circular_queue(5)
a.cq_add(1)
a.cq_add(2)
a.cq_add(3)
a.cq_add(4)
a.cq_add(5)
a.cq_delete()
a.cq_add(10)
a.cq_add(15) # circular queue is full
a.cq_delete()
a.cq_delete()
a.cq_delete()
a.cq_delete()
a.cq_delete()
a.cq_delete()




