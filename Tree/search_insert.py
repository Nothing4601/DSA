class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def insert(root,value):
    if root is None:
        return Node(value) # return address of new;y created Node
    if root.data==value:
        return root
    elif root.data < value:
        insert(root.right,value)
    else:
        insert(root.left,value)

