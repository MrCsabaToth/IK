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
    uni_value_counter = 0

    def uni_value_helper(self, node: TreeNode):
        # Leaf
        if not node.left and not node.right:
            self.uni_value_counter += 1
            return True

        i_am_univalue = True
        if node.left:
            bL = self.uni_value_helper(node.left)
            if not bL or node.val != node.left.val:
                i_am_univalue = False
            

        if node.right:
            bL = self.uni_value_helper(node.right)
            if not bL or node.val != node.right.val:
                i_am_univalue = False

        if i_am_univalue:
            self.uni_value_counter += 1

        return i_am_univalue

    def uni_value(self, root: TreeNode):
        if root is None:
            return 0

        _ = self.uni_value_helper(root)
        return self.uni_value_counter


import pytest

@pytest.mark.parametrize("values,expected", [
    ([5, 1, 5, 5, 5, None, 5], 4),
    ([5, 1, 5, 5, 5, None, 5, 5, 5], 6),
])
def test_uni_value(values, expected):
    tree = TreeNode.buildTree(values)
    solution = Solution()
    assert solution.uni_value(tree) == expected

pytest.main()

