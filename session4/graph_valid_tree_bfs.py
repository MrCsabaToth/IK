# 261
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [False] * n
        parent = [None] * n
        adj_list = [None] * n
        for vertex in range(n):
            adj_list[vertex] = list()
            parent[vertex] = list()

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        def bfs(source):
            q = []
            q.append(source)
            visited[source] = True
            while q:
                node = q.pop(0)
                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        parent[neighbor].append(node)
                        q.append(neighbor)
                    else:
                        if neighbor not in parent[node]:
                            # Cross edge
                            return True

            return False

        has_cycle = bfs(vertex)
        if has_cycle:
            return False

        return all(node for node in visited)
