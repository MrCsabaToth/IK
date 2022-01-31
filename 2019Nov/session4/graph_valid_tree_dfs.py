class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [False] * n
        parent = [None] * n
        adj_list = [None] * n
        for vertex in range(n):
            adj_list[vertex] = list()

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        def dfs(source):
            visited[source] = True
            for neighbor in adj_list[source]:
                if not visited[neighbor]:
                    parent[neighbor] = source
                    if dfs(neighbor):
                        return True
                else:
                    if neighbor != parent[source]:
                        # Cross edge
                        return True

            return False

        has_cycle = dfs(vertex)
        if has_cycle:
            return False

        return all(node for node in visited)
