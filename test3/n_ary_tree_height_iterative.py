'''
    For your reference:
    
    class TreeNode:
        def __init__(self):
            self.children = []

'''

# Perform a DFS but at each leaf perform max
def find_height(root):
    maxh = 0

    if not root:
        return maxh

    queue = [(root, 0)]
    while queue:
        node, level = queue.pop()
        if not node.children:
            if level > maxh:
                maxh = level

        for n in node.children:
            queue.append((n, level + 1))

    return maxh
