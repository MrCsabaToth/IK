'''
    For your reference:
    
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

LEFT = 0
RIGHT = 1

def build_balanced_bst(a):
    start = 0
    end = len(a) - 1
    mid = end // 2
    root = TreeNode(a[mid])
    stack = [(root, mid + 1, end, RIGHT), (root, start, mid - 1, LEFT)]

    while stack:
        parent, start, end, direction = stack.pop()
        if start > end:
            continue

        mid = start + (end - start) // 2
        node = TreeNode(a[mid])
        if direction == LEFT:
            parent.left_ptr = node
        else:  # direction == RIGHT
            parent.right_ptr = node

        stack.append((node, mid + 1, end, RIGHT))
        stack.append((node, start, mid - 1, LEFT))

    return root
