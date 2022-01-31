# For your reference:
#
# class Node:
#     def __init__(self):
#         self.val = 0
#         self.neighbours = []

def build_other_graph(node):
    q = [node]
    node_map = {node.val: Node(node.val)}
    while q:
        vertex = q.pop()
        for neighbor in vertex.neighbours:
            if neighbor.val not in node_map:
                node_map[neighbor.val] = Node(neighbor.val)

            neighbor.neighbours.append(node_map[vertex.val])
            q.append(neighbor)

    return node_map[vertex.val]
