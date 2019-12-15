def findCriticalConnections(noOfServers, noOfConnections, connections):
    critical = []
    visited = [False] * noOfServers

    def dfs(source):
        visited[source] = True
        for neighbor in adj_list[source]:
            if not visited[neighbor]:
                dfs(neighbor)

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

        dfs(0)    

        if any(v is False for v in visited):
            critical.append(connection)

    return critical if critical else [(-1, -1)]
