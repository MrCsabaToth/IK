'''
    For your reference:
    
    class TreeNode:
        def __init__(self):
            self.children = []

'''

# Perform a DFS but at each leaf perform max
# Pass along the level in recursive calls

def find_height(root):
    def dfs_helper(node, level, hmax):
        if not node.children:
            if level > hmax[0]:
                hmax[0] = level

            return

        for n in node.children:
            dfs_helper(n, level + 1, hmax)

    height = [0]
    dfs_helper(root, 0, height)
    return height[0]
