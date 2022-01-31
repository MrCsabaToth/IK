# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below
# Input: root of the input tree
# Output: A list of integer lists denoting the node values of the paths of the tree

paths = []

def allPathsOfABinaryTree(root):
    def pathHelper(node, stack):
        if not node:
            return

        stack.append(node.val)
        if not node.left_ptr and not node.right_ptr:
            paths.append(stack[:])

        pathHelper(node.left_ptr, stack)
        pathHelper(node.right_ptr, stack)
        stack.pop()

    pathHelper(root, [])
    return paths
