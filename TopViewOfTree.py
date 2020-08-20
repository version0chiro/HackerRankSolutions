class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def fillMap(root, d, l, m): 
    if(root == None): 
        return
      
    if d not in m: 
        m[d] = [root.info,l] 
    elif(m[d][1] > l): 
        m[d] = [root.info,l] 
    fillMap(root.left, d - 1, l + 1, m) 
    fillMap(root.right, d + 1, l + 1, m) 
  
# function should prthe topView of 
# the binary tree 
def topView(root): 
      
    # map to store the pair of node value and its level  
    # with respect to the vertical distance from root.  
    m = {} 
      
    fillMap(root, 0, 0, m) 
    for it in sorted (m.keys()): 
        print(m[it][0], end = " ")
        
