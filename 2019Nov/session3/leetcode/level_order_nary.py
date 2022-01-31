# Leetcode 429

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        solution = []
        if root is None:
            return solution

        queue = [root]
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                for n in node.children:
                    queue.append(n)

            solution.append(level)

        return solution
