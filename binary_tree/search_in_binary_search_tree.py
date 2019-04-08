class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def searchBST(root, val):
    if root and val < root.val: 
        return searchBST(root.left, val)
     
    elif root and val > root.val:
        return searchBST(root.right, val)   
        
    return root
