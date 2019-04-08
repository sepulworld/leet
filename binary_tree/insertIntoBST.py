class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    
    if root.val > val:
        root.left = insertIntoBST(root.left, val)
   
    else:
        root.right = insertIntoBST(root.right, val)
         
    return root
