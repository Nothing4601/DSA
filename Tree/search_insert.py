# For all below question we have tp print Inorder traversal in BST
#    i)Print all element of BST in incresing order
#    ii)How to check a valid BST
#    iii)Inoreder Traversal of BST

class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

# Insert 'value' in BST whose Root node  is 'root'
def insert(root,value):

    if root is None:
        return Node(value) # return address of newly created Node
    if root.data==value:
        return root
    elif root.data < value:
        root.right = insert(root.right,value)
    else:
        root.left = insert(root.left,value)
    return root # return root so the parent node keeps pointing to the updated subtree after insertion

def search(root,value):
    if root is None:
        print('Element not found')
        return 
    if root.data == value:
        print('Element Found!')
    elif root.data < value:
        search(root.right,value)
    else:
        search(root.left,value)
    return

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

root = insert(None, 5) # or root = Node(5)  --> both will make Root node of tree 
print(root)

insert(root,4)
insert(root,3)
insert(root,3.5)
insert(root,6)
insert(root,6.5)
insert(root,9)
insert(root,8)
insert(root,0)
inorder(root)

print(root)
search(root,9)
search(root,2)
print(search(root,0))