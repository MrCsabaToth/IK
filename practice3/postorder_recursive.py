# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

traversal = []

def postorderTraversal(root):

    def postorderHelper(node):
        if not node:
            return
    
        postorderTraversal(node.left_ptr)
        postorderTraversal(node.right_ptr)
        traversal.append(node.val)

    postorderHelper(root)
    return traversal
