# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

def flipUpsideDown(root):
    if not root:
        return None

    node = root
    stack = [(root, None, None)]
    while node and node.left_ptr:
        save_left = node.left_ptr
        stack.append((node.left_ptr, node.right_ptr, node))
        node = node.left_ptr

    new_root = node

    while stack:
        node, left, right = stack.pop()
        node.left_ptr = left
        node.right_ptr = right

    return new_root
