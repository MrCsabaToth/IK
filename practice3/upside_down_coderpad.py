class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

    def __str__(self):
        return "{}<{}, {}>".format(self.val, self.left_ptr.val if self.left_ptr else None,
                                   self.right_ptr.val if self.right_ptr else None)

    @staticmethod
    def buildTree(values):
        nodes = [None] + [(TreeNode(val) if val != None else None) for val in values]
        length = len(nodes)
        for i, node in enumerate(nodes):
            if i == 0 or not node:
                continue

            left_idx = i * 2
            if left_idx < length:
                node.left_ptr = nodes[left_idx]
            right_idx = i * 2 + 1
            if right_idx < length:
                node.right_ptr = nodes[right_idx]

        return nodes[1]

    def to_array_helper(self, array, index):
        array[index] = self.val
        if self.left_ptr:
            self.left_ptr.to_array_helper(array, index * 2)

        if self.right_ptr:
            self.right_ptr.to_array_helper(array, index * 2 + 1)

    def to_array(self):
        array = [None] * 2 ** 5
        self.to_array_helper(array, 1)
        for i in range(len(array) - 1, 0, -1):
            if array[i] is not None:
                break

        return array[1:i + 1]

    def traverse(self):
        arr = []
        if self.left_ptr:
            arr.extend(self.left_ptr.traverse())

        arr.append(self.val)

        if self.right_ptr:
            arr.extend(self.right_ptr.traverse())

        return arr


def flipUpsideDown(root):
    node = root
    stack = [(root, None, None)]
    while node and node.left_ptr:
        stack.append((node.left_ptr, node.right_ptr, node))
        node = node.left_ptr

    new_root = node

    while stack:
        node, left, right = stack.pop()
        node.left_ptr = left
        node.right_ptr = right

    return new_root


import pytest

def test_flip_upside_down():
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    values = [1, 2, 3, 4, 5, None, None]
    tree = TreeNode.buildTree(values)
    #   4
    #  / \
    # 5   2
    #    / \
    #   3   1
    values2 = [4, 5, 2, None, None, 3, 1]
    tree2 = TreeNode.buildTree(values2)
    expected = tree2.to_array()
    upside_down = flipUpsideDown(tree)
    # print(upside_down.traverse())
    assert upside_down.to_array() == expected

pytest.main()
