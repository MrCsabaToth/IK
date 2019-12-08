'''
    For your reference:
    
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

INIT = 0
PROC = 1
POST = 2

# Concept: An in order walk produces sorted order list.
# Start a tree walk until we reach kth.
def kth_smallest_element(root, k):
    stack = [(root, INIT)]  # reverse order stack

    i = 0
    while stack:
        node, state = stack.pop()
        if not node:
            continue

        if state == INIT:
            stack.append((node.right_ptr, INIT))
            stack.append((node, PROC))
            stack.append((node.left_ptr, INIT))
        else:  # state = PROC
            i += 1
            if i == k:
                return node.val

    return None
