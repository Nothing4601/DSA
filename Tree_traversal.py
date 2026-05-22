# Binary tree (max 2 child) :
#    i)Binary search tree : left of node is less than right of node
#    ii)Full(Strict) Binary tree : Only 0 or 2 child 
#    iii)Complete Binary tree : only go to next level when previous level is full (start form left to right)
#    iv)Skew and Degenerate Binary tree: just like linear data structure

# Two Ways of implementation :
#    i) Arrays : memory wastage, leave some space as apply fomrula for finding child index
#                  left_child_index = Parent_index*2 + 1 
#                  right_child_index = Parent_index*2 + 2
#    ii) Linked List

# Class to make node
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

  #Preorder = Root --> Left --> Right
    def preorder(self,root_node): 
        if root_node != None:
          print(root_node.data, end=' ')
          self.preorder(root_node.left)
          self.preorder(root_node.right)

  #Inorder = left --> root --> right
    def inorder(self,root_node): 
        if root_node != None:
           self.inorder(root_node.left)
           print(root_node.data, end=' ')
           self.inorder(root_node.right)
    
  #Postorder = left --> right --> root
    def postorder(self,root_node): 
        if root_node != None:
           self.postorder(root_node.left)
           self.postorder(root_node.right)
           print(root_node.data, end=' ')

    # Why below code is wrong :| ,  issue with self.rn = root_node 
    # def preorder(self,root_node): 
    #     self.rn = root_node
    #     if self.rn:
    #       print(self.rn.data, end=' ')
    #       self.preorder(self.rn.left)
    #       self.preorder(self.rn.right)

# making a tree
rn =Node(1)
rn.left = Node(0)
rn.right = Node(2)
rn.left.left = Node(-1)
rn.right.left = Node(1.5)
rn.right.right = Node(3)

#printing tree
print('Preorder =',end=' ')
rn.preorder(rn)
print('\n','Inorder =',end=' ')
rn.inorder(rn)
print('\n','Postorder =',end=' ')
rn.postorder(rn)