# Terminology :
#    i) Inorder Successor : the node that is visited immediately after a given target node during an inorder traversal
#        how to get : One step towards right --> leftmost element
#    ii) Inorder Predessor : 
#        how to get : One step towards left --> rightmost element 

#BST deletion handles three cases based on child count
#   i) Zero child (leaf deletion)
#   ii) One child
#   iii) Two child

#finding successor of root 
def get_successor(root):
    if root:
       root=root.right
       while(root.left!=None and root is not None):
           root=root.left
    return root   # return address of successor

# finding predessor of root
def get_predessor(root):
    if root:
       root=root.left
       while(root.right and root is not None):
           root=root.right
    return root

def deletion(root,value):
    if root is None:
        print(f'\n{value} is not present in the tree to delete')
        return
    if root.data == value : # we reach at the root which we have to delete
    # below code delete node who has either '0' or '1' child
        
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
    # below else part will handle case when root has both child
        else:
            succ = get_successor(root) # succ --> address of successor
            root.data = succ.data
            root.right = deletion(root.right, succ.data)
            
    elif root.data < value:
        root.right = deletion(root.right,value)
    else:
        root.left = deletion(root.left,value)
    return root

class Node:
    def __init__(self,data):
        self.data= data
        self.right = None
        self.left = None

def insert(root,value):
    if root is None:
        return Node(value)
    if root.data==value:
        return root
    elif root.data<value:
        root.right=insert(root.right,value)
    else:
        root.left= insert(root.left,value)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

root = Node(5)
insert(root,2)
insert(root,0)
insert(root,-3)
insert(root,6)
insert(root,8)
insert(root,2.5)
inorder(root)
deletion(root,2)
print('\n')
inorder(root)
