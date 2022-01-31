# Leetcode 112
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
    def path_sum(self, node, partial_sum):
        # Leaf node case
        if node.left is None and node.right is None:
            return partial_sum == node.val

        # Recursion
        return (
            node.left and self.path_sum(node.left, partial_sum - node.val)
            or
            node.right and self.path_sum(node.right, partial_sum - node.val)
        )


import pytest

def test_path_sum():
    #      5
    #     / \
    #    4   8
    #   /   / \
    #  11  13  4
    # /  \      \
    #7    2      1
    values = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    tree = TreeNode.buildTree(values)
    summ = 22
    expected = True
    solution = Solution()
    assert solution.path_sum(tree, summ) == expected

pytest.main()

