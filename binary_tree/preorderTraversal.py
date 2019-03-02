class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.output = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            print(f'TreeNode value: {root.val}')
            print(f'TreeNode left: {root.left}')
            print(f'TreeNode right: {root.right}')
            self.output.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.output
