# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    solutions = []

    def pathSumHelper(self, node, stack, partialSum):
        if not node:
            return

        stack.append(node.val)
        if not node.left and not node.right:
            if node.val == partialSum:
                self.solutions.append(stack[:])
        else:
            partSum = partialSum - node.val
            self.pathSumHelper(node.left, stack, partSum)
            self.pathSumHelper(node.right, stack, partSum)

        stack.pop()

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.solutions = []
        if root:
            self.pathSumHelper(root, [], sum)

        return self.solutions
