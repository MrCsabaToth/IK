# 785
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = dict()
        adj_list = dict()

        # Interpreting input
        for i, nodes in enumerate(graph):
            visited[i] = False
            adj_list[i] = nodes
#             for node in nodes:
#                 if node in visited:
#                     if i not in adj_list[node]:
#                         adj_list[node].append(i)
#                 else:
#                     visited[node] = False
#                     adj_list[node] = [i]

#                 if node not in adj_list[i]:
#                     adj_list[i].append(node)

        # Alternating coloring DFS
        def dfs(source, color):
            visited[source] = color
            for neighbor in adj_list[source]:
                if visited[neighbor] is False:
                    if dfs(neighbor, 0 if color else 1):
                        return True
                elif visited[neighbor] == color:
                    # Cross edge
                    return True

            return False

        # Able to handle multi components as well
        components = 0
        for vertex in visited.keys():
            if visited[vertex] is False:
                components += 1
                problem = dfs(vertex, 0)
                if problem:
                    return False

        return all(color is not False for color in visited.values())
