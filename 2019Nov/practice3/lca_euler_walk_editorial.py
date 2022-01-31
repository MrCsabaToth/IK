#class Node(object):
#    def __init__(self, data, left=None, right=None):
#        self.data = data
#        self.left = left
#        self.right = right

euler = dict(
    walk=[],
    levels=[],
)

def lca(root, a, b):
    def add_euler(data, level):
        euler['walk'].append(data)
        euler['levels'].append(level)

    def dfs(node, level):
        if not node:
            return

        add_euler(node.data, level)

        if node.left:
            dfs(node.left, level + 1)
            add_euler(node.data, level)

        if node.right:
            dfs(node.right, level + 1)
            add_euler(node.data, level)

    euler['walk'] = []
    euler['levels'] = []
    dfs(root, 0)

    ai = euler['walk'].index(a.data)
    bi = euler['walk'].index(b.data)
    idx_with_min_level = None
    min_level = 10e6
    for x in range(ai + 1, bi):
        if euler['levels'][x] < min_level:
            min_level = euler['levels'][x]
            idx_with_min_level = x

    return euler['walk'][idx_with_min_level]
