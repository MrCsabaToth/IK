'''
    For your reference:
    
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

def build_balanced_bst(a):
    def builder(a, start, end):
        if start > end:
            return None

        # Overflow avoidance - Omkar
        mid = start + (end - start) // 2
        node = TreeNode(a[mid])
        node.left_ptr = builder(a, start, mid - 1)
        node.right_ptr = builder(a, mid + 1, end)
        return node

    return builder(a, 0, len(a) - 1)
