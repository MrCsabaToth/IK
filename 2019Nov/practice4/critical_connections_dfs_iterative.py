def findCriticalConnections(noOfServers, noOfConnections, connections):
    critical = []

    for connection in connections:
        adj_list = [None] * noOfServers
        visited = [False] * noOfServers
        edges = connections[:]
        edges.remove(connection)

        for vertex in range(noOfServers):
            adj_list[vertex] = list()
    
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        q = [0]
        while q:
            node = q.pop()
            visited[node] = True

            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    q.append(neighbor)

        if any(v is False for v in visited):
            critical.append(connection)

    return critical if critical else [(-1, -1)]
