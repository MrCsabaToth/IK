# Leetcode 105
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

    def is_strictly_balanced(self):
        return False


class Solution:
    inorder_indexes = dict()

    def build_tree(self, preorder, inorder):
        for i, val in enumerate(inorder):
            self.inorder_indexes[inorder[i]] = i

        return self.build_tree_helper(preorder, inorder)

    def build_tree_helper(self, preorder, start_p, end_p, inorder, start_i, end_i):
        if start_p > end_p or not preorder:
            return None

        root = TreeNode(preorder[start_p])
        # could be ommitted
        if start_p == end_p:
            return root

        root_index = self.inorder_indexes[root.val]
        num_left = root_index - start_i
        # num_right = end_i - root_index
        root.left = self.build_tree_helper(preorder, start_p + 1, start_p + num_left, inorder, start_i, root_index - 1)
        root.right = self.build_tree_helper(preorder, start_p + num_left + 1, end_p, inorder, root_index + 1, end_i)
        return root


import pytest

def test_path_sum():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    expected = [0, -3, 9, -10, None, 5]
    solution = Solution()
    assert solution.build_tree(preorder, inorder) == expected

pytest.main()

