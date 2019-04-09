class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.initial_value = None
        self.false_count = 0
        
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return None
        
        if not self.initial_value:
            self.initial_value = root.val
        
        self.isUnivalTree(root.left)
        self.isUnivalTree(root.right)
        
        if root.val != self.initial_value:
            self.false_count += 1
            
        if self.false_count > 0:
            return False
        else:
            return True
