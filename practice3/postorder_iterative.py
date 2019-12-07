# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

traversal = []

PRE = 1
PROCESS = 2
POST = 3  # not used

def postorderTraversal(root):

    def postorderHelper(root):
        stack = [(root, PRE)]

        while stack:
            node, state = stack.pop()
            if not node:
                continue

            if state == PRE:
                stack.append((node, PROCESS))
                stack.append((node.right_ptr, PRE))
                stack.append((node.left_ptr, PRE))
            elif state == PROCESS:
                traversal.append(node.val)

    postorderHelper(root)
    return traversal
