# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    solutions = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.solutions = []
        if not root:
            return self.solutions

        stack = [(root, 0, root.val)]
        partial = [root.val]
        while stack:
            node, level, part_sum = stack.pop()
            partial = partial[:level]
            partial.append(node.val)

            if not node.left and not node.right:
                if part_sum == sum:
                    self.solutions.append(partial[:])

            else:
                if node.left:
                    stack.append((node.left, level + 1, part_sum + node.left.val))

                if node.right:
                    stack.append((node.right, level + 1, part_sum + node.right.val))

        return self.solutions
