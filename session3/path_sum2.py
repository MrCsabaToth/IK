# Leetcode 113
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
    solutions = []

    def path_sum2(self, node, stack, partial_sum):
        if not node:
            return

        stack.append(node.val)
        # Leaf node case
        if node.left is None and node.right is None:
            if partial_sum == node.val:
                self.solutions.append(stack[:])
                print(node.val, stack, self.solutions)
        else:
            # Recursion
            remainder_sum = partial_sum - node.val
            self.path_sum2(node.left, stack, remainder_sum)
            self.path_sum2(node.right, stack, remainder_sum)

        stack.pop()


import pytest

def test_path_sum():
    #      5
    #     / \
    #    4   8
    #   /   / \
    #  11  13  4
    # /  \    / \
    #7    2  5   1
    values = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    tree = TreeNode.buildTree(values)
    # print(tree.to_array(), values)
    summ = 22
    expected = [
       [5, 4, 11, 2],
       [5, 8, 4, 5]
    ]
    solution = Solution()
    solution.path_sum2(tree, [], summ)
    assert solution.solutions == expected

pytest.main()

