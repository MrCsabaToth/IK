# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        # Leaf node
        if not root.left and not root.right:
            return sum == root.val

        partial = sum - root.val
        return (
            root.left and self.hasPathSum(root.left, partial) or
            root.right and self.hasPathSum(root.right, partial)
        )
