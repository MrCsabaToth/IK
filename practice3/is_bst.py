# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def isBST(root):
    def isBSTHelper(node, lower, upper):
        if not node:
            return True

        return (
            node.val >= lower and
            node.val <= upper and
            isBSTHelper(node.left_ptr, lower, node.val) and
            isBSTHelper(node.right_ptr, node.val, upper)
        )

    return isBSTHelper(root, -10e9, 10e9)
