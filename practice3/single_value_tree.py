# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def findSingleValueTrees(root):
    counter = [0]

    def unival_helper(node):
        # Leaf node
        if not node.left_ptr and not node.right_ptr:
            counter[0] += 1
            return True

        # Intermediate node
        uni_left = node.left_ptr and unival_helper(node.left_ptr)
        left_uni = not node.left_ptr or node.left_ptr.val == node.val and uni_left

        uni_right = node.right_ptr and unival_helper(node.right_ptr)
        right_uni = not node.right_ptr or node.right_ptr.val == node.val and uni_right

        my_uni = left_uni and right_uni
        if my_uni:
            counter[0] += 1

        return my_uni

    if root:
        unival_helper(root)

    return counter[0]
