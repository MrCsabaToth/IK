# Leetcode 108
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

    def heights(self):
        if not self.left and not self.right:
            return 0, 0

        max_height = 0
        min_height = 0
        left_max_height, left_min_heigt = self.left.height() if self.left else 0, 0
        right_max_height, right_min_heigt = self.right.height() if self.right else 0, 0
        return max(left_max_height, right_max_height), min(left_min_heigt, right_min_heigt)

    def is_strictly_balanced(self):
        return False

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
    def build_balanced_tree(self, sorted_array):
        return self.build_balanced_tree_helper(sorted_array, 0, len(sorted_array) - 1)

    def build_balanced_tree_helper(self, sorted_array, start, end):
        if start > end:
            return None

        # Could be ommitted
        # if start == end:
        #     return TreeNode(sorted_array[start])

        # overflow avoidance trick
        mid = start + (end - start) // 2

        root = TreeNode(sorted_array[mid])
        root.left = self.build_balanced_tree_helper(sorted_array, start, mid - 1)
        root.right = self.build_balanced_tree_helper(sorted_array, mid + 1, end)
        return root


import pytest

def test_path_sum():
    values = [-10, -3, 0, 5, 9]
    expected = [0, -3, 9, -10, None, 5]
    # [0, -10, 5, None, -3, None, 9]
    solution = Solution()
    root = solution.build_balanced_tree(values)
    print(root.val, root.to_array())
    assert root.to_array() == expected

pytest.main()

