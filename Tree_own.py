# make node class
class node:
    def __init__(self,data,left=None,right= None):
        self.data= data
        self.left = left
        self.right= right
    
class tree:
    def __init__(self,root_node):
        temp = node(root_node)
        self.rn = temp

    def insertAtL(self,data):
        t1 = node(data)
        if self.rn == None:
            self.rn=t1
            return 
        while(self.rn.left != None):
            self.rn = self.rn.left
        self.rn.left = t1

    def insertAtR(self,data):
        t1 = node(data)
        if self.rn == None:
            self.rn=t1
            return 
        while(self.rn.right != None):
            self.rn = self.rn.right
        self.rn.right = t1

tree1= tree(1)
tree1.insertAtL(2)
tree1.insertAtR(3)
tree1.insertAtL(4)
tree1.insertAtR(7)
