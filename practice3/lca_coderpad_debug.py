# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    def __str__(self):
        return "{}<{}, {}>".format(self.data, self.left.data if self.left else None,
                                   self.right.data if self.right else None)

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


paths = dict(
    a=[],
    b=[],
    solution=None
)

def lca(root, a, b):
    def dfs(node, stack):
        if not node or paths['solution'] is not None:
            return

        stack.append(node.data)

        if node.data == a:
            paths['a'] = stack[:]
        if node.data == b:
            paths['b'] = stack[:]

        if paths['a'] and paths['b']:
            a_rev = paths['a'][::-1]
            b_rev = paths['b'][::-1]
            print(paths['a'], paths['b'], a_rev, b_rev)
            for num in a_rev:
                if num in b_rev:
                    paths['solution'] = num
                    return

        dfs(node.left, stack)
        dfs(node.right, stack)

        stack.pop()

    dfs(root, [])
    return paths['solution']


import pytest

@pytest.mark.parametrize("a,b,expected", [
    (7, 2, 11),
    (13, 6, 8),
    (13, 1, 8),
    (13, 2, 5),
    (7, 1, 5),
    (2, 1, 5),
    (11, 1, 5),
])
def test_path_sum(a, b, expected):
    #      5
    #     / \
    #    4   8
    #   /   / \
    #  11  13  6
    # /  \      \
    #7    2      1
    values = [5, 4, 8, 11, None, 13, 6, 7, 2, None, None, None, None, None, 1]
    tree = TreeNode.buildTree(values)
    paths['a'] = []
    paths['b'] = []
    paths['solution'] = None
    assert lca(tree, a, b) == expected

pytest.main()

