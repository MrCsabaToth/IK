# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return []

        visit = [(root, 0)]
        stack = []

        while stack:
            node, partial = stack.pop()
            if not node:
                continue

            if not node.left and not node.right:
                if partial + node.val == sum:
                    return True
            else:
                part_sum = partial + node.val
                stack.append((node.left, part_sum))
                stack.append((node.right, part_sum))

        return False
