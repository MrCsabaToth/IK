def shortest_solution():
    solutions = []
    shortcuts = {
        1: 38,
        4: 14,
        9: 31,
        17: 7,
        21: 42,
        28: 84,
        51: 67,
        54: 34,
        62: 19,
        64: 60,
        72: 91,
        80: 99,
        87: 36,
        93: 73,
        95: 75,
        98: 79,
    }
    # Generate board
    n = 101
    adj_list = dict()
    for i in range(n):
        adj_list[i] = [(j + i if j + i not in shortcuts else shortcuts[j + i], j) for j in range(1, 7) if j + i <= 100]


    def bfs(node, distance, path):
        if node == 100:
            
        q = []
        q.append(node)
        visited[node] = True
        while q:
            node = q.pop(0)
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor].append(node)
                    q.append(neighbor)

    bfs(0, 0, [False] * n)
