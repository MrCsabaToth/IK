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

    def to_array_helper(self, array, index):
        array[index] = self.val
        if self.left:
            self.left.to_array_helper(array, index * 2)

        if self.right:
            self.right.to_array_helper(array, index * 2 + 1)

    def to_array(self):
        array = [None] * 2 ** 6
        self.to_array_helper(array, 1)
        for i in range(len(array) - 1, 0, -1):
            if array[i] is not None:
                break

        return array[1:i + 1]


class Solution:
    inorder_indexes = dict()

    def build_tree(self, preorder, inorder):
        for i, val in enumerate(inorder):
            self.inorder_indexes[inorder[i]] = i

        return self.build_tree_helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

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
    #    3
    #   / \
    #  9  20
    #    /  \
    #   15   7
    expected = [3, 9, 20, None, None, 15, 7]
    solution = Solution()
    root = solution.build_tree(preorder, inorder)
    assert root.to_array() == expected

pytest.main()

