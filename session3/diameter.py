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
    max_diam = 0

    def diameter_helper(self, node: TreeNode):
        # Leaf
        if not node.left and not node.right:
            return 0

        my_height = 0
        my_diam = 0
        if node.left:
            left_height = self.diameter_helper(node.left)
            my_diam = left_height + 1
            my_height = my_diam
            

        if node.right:
            right_height = self.diameter_helper(node.right)
            my_diam += right_height + 1
            my_height = max(my_height, right_height + 1)

        self.max_diam = max(self.max_diam, my_diam)
        return my_height

    def diameter(self, root: TreeNode):
        if root is None:
            return 0

        _ = self.diameter_helper(root)
        return self.max_diam


import pytest

@pytest.mark.parametrize("values,expected", [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, None, 4, 5, None, None, 3, 6], 3),
])
def test_diameter(values, expected):
    tree = TreeNode.buildTree(values)
    solution = Solution()
    assert solution.diameter(tree) == expected

pytest.main()

