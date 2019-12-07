#class Node(object):
#    def __init__(self, data, left=None, right=None):
#        self.data = data
#        self.left = left
#        self.right = right

paths = dict(
    a=[],
    b=[],
    solution=None
)

def lca(root, a, b):
    def dfs(node, stack):
        if not node or paths['solution'] is not None:
            return

        stack.append(node)

        if node == a:
            paths['a'] = stack[:]
        if node == b:
            paths['b'] = stack[:]

        if paths['a'] and paths['b']:
            a_rev = paths['a'][::-1]
            b_rev = paths['b'][::-1]
            for node_a in a_rev:
                if node_a in b_rev:
                    paths['solution'] = node_a.data
                    return

        dfs(node.left, stack)
        dfs(node.right, stack)

        stack.pop()

    paths['a'] = []
    paths['b'] = []
    paths['solution'] = None
    dfs(root, [])
    return paths['solution']
