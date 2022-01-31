# Complete the function below.

def find_order(words):
    if not words:
        return []

    n = len(words)

    nodes = []
    adj_list = []

    # 1. Take each word pair
    for i, word in enumerate(words):
        if i >= n - 1:
            break

        word2 = words[i + 1]
        # 2. Find first character which differs
        for j, ch in enumerate(word):
            if ch != word2[j]:
                # 3. Means a graph edge
                # 3.1. Optionally register node1 for ch1
                if ch not in nodes:
                    nodes.append(ch)
                    adj_list.append([])

                node1 = nodes.index(ch)

                # 3.2. Optionally register node2 for ch2
                ch2 = word2[j]
                if ch2 not in nodes:
                    nodes.append(ch2)
                    adj_list.append([])

                node2 = nodes.index(ch2)

                # 3.3. Register edge
                if node2 not in adj_list[node1]:
                    adj_list[node1].append(node2)

                break

    visited = [False] * n
    # 4. Topological sort
    def topo_sort_dfs(vertex, st):
        visited[vertex] = True
        for neighbor in adj_list[vertex]:
            topo_sort_dfs(vertex, st)

        st.insert(0, vertex)

    stack = []
    for v in range(n):
        if not visited[v]:
            topo_sort_dfs(v, stack)

    return "".join(stack)
