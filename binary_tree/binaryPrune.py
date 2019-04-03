class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    """"https://leetcode.com/problems/binary-tree-pruning/"""
    def pruneTree(self, root):
        if not root:
            print(f'no root {root}')
            return None
       
        # recursive use of pruneTree 
        print(f'there is a root, and here is the node vaules: {root.__dict__}')
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if not root.left and not root.right and not root.val:
            print(f'no left, no right, no val: {root.__dict__}')
            return None

        # base result 
        print(f'processed node done: {root.__dict__}')        
        return root


# For input [1, null, 0, 0, 1]

"""
there is a root, and here is the node vaules: {'val': 1, 'left': None, 'right': <precompiled.treenode.TreeNode object at 0x7f7e64c92ef0>}
no root None
there is a root, and here is the node vaules: {'val': 0, 'left': <precompiled.treenode.TreeNode object at 0x7f7e64c92f28>, 'right': <precompiled.treenode.TreeNode object at 0x7f7e64c9a748>}
there is a root, and here is the node vaules: {'val': 0, 'left': None, 'right': None}
no root None
no root None
no left, no right, no val: {'val': 0, 'left': None, 'right': None}
there is a root, and here is the node vaules: {'val': 1, 'left': None, 'right': None}
no root None
no root None
processed node done: {'val': 1, 'left': None, 'right': None}
processed node done: {'val': 0, 'left': None, 'right': <precompiled.treenode.TreeNode object at 0x7f7e64c9a748>}
processed node done: {'val': 1, 'left': None, 'right': <precompiled.treenode.TreeNode object at 0x7f7e64c92ef0>}
"""

