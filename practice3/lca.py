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

        stack.append(node.data)

        if node.data == a:
            paths['a'] = stack[:]
        if node.data == b:
            paths['b'] = stack[:]

        if len(paths['a']) and len(paths['b']):
            a_rev = paths['a'][::-1]
            b_rev = paths['b'][::-1]
            for num in a_rev:
                if num in b_rev:
                    paths['solution'] = num
                    return

        dfs(node.left, stack)
        dfs(node.right, stack)

        stack.pop()

    paths['a'] = []
    paths['b'] = []
    paths['solution'] = None
    dfs(root, [])
    return paths['solution']