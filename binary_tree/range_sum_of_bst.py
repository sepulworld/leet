total_sum = 0

def rangeSumBST(root, L, R):
    """https://leetcode.com/problems/range-sum-of-bst/"""
    if root:
        if root.val > L and root.val < R:
            total_sum += root.val
        rangeSumBST(root.left, L, R)
        rangeSumBST(root.right, L, R)
    
    return total_sum + L + R