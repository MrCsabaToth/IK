# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "{}<{}, {}>".format(self.val, self.left.val if self.left else None, self.right.val if self.right else None)

    @staticmethod
    def buildTree(values):
        nodes = [None] + [(TreeNode(val) if val != None else None) for val in values]
        length = len(nodes)
        for i, node in enumerate(nodes):
            if i == 0 or not node:
                continue

            left_idx = i * 2
            if left_idx < length:
                node.left = nodes[left_idx]
            right_idx = i * 2 + 1
            if right_idx < length:
                node.right = nodes[right_idx]

        return nodes[1]

class Solution:
    def levelOrder1(self, root: TreeNode):
        result  = []
        if root is None:
            return result

        queue = [root, "EOL"]
        line = []
        while queue:
            node = queue.pop(0)
            if node == "EOL":
                result.append(line)
                line = []
                if queue: # and queue[-1] != "EOL":
                    queue.append("EOL")

                continue

            elif node is None:
                continue

            line.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def levelOrder2(self, root: TreeNode):
        result  = []
        if root is None:
            return result

        queue = [root]
        while queue:
            node_count = len(queue)
            line = []
            for _ in range(node_count):
                node = queue.pop(0)

                line.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(line)

        return result


import pytest

def test_level_order():
    values = [3, 9, 20, None, None, 15, 7]
    tree = TreeNode.buildTree(values)
    expected = [
      [3],
      [9, 20],
      [15, 7]
    ]
    solution = Solution()
    assert solution.levelOrder1(tree) == expected
    assert solution.levelOrder2(tree) == expected

pytest.main()

