class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TraverseTree:
    def __init__(self):
        self.output = []
   
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.output.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.output 
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.output.append(root.val)
        return self.output
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            self.output.append(root.val)
            self.inorderTraversal(root.right)
        return self.output
