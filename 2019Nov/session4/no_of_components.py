# Leetcode 323
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        adj_list = [None] * n
        for vertex in range(n):
            adj_list[vertex] = list()

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        # 96 ms, faster than 9x%
        def bfs(source):
            q = []
            q.append(source)
            visited[source] = True
            while q:
                node = q.pop(0)
                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)

        # 116 ms, faster than 67.25%
        def dfs(source):
            q = []
            q.append(source)
            visited[source] = True
            while q:
                node = q.pop()
                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)

        components = 0
        for vertex in range(n):
            if not visited[vertex]:
                components += 1
                dfs(vertex)

        return components
