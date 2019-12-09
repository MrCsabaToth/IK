'''
    For your reference:
    
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

def kth_smallest_element(root, k):
    def traverse(node, index):
        if not node:
            return None

        left_result = traverse(node.left_ptr, index)
        if left_result is not None:
            return left_result

        index[0] += 1
        if index[0] == k:
            return node.val

        if index[0] < k:
            return traverse(node.right_ptr, index)

        return None

    if not root:
        return None

    return traverse(root, [0])
