'''
    For your reference:
    
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

# Concept: An in order walk produces sorted order list.
# Start a tree walk until we reach kth.
def kth_smallest_element(root, k):

    def walk_helper(node, counter):
        if not node:
            return None

        left_search = walk_helper(node.left_ptr, counter)
        if left_search is not None:
            return left_search

        counter[0] += 1
        if counter[0] == k:
            return node.val

        # right search
        return walk_helper(node.right_ptr, counter)

    return walk_helper(root, [0])
