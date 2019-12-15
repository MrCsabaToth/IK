class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Underspecified input 0
        if not words:
            return []

        n = len(words)
        # Underspecified input 1
        if n == 1:
            return "".join(set(list(words[0])))

        nodes = []
        adj_list = []

        # 1. Take each word pair
        for i, word in enumerate(words[:-1]):
            word2 = words[i + 1]
            len2 = len(word2)
            # 2. Find first character which differs
            for j, ch in enumerate(word):
                # 3.1. Optionally register node1 for ch1
                if ch not in nodes:
                    nodes.append(ch)
                    adj_list.append([])

                node1 = nodes.index(ch)
                if j <= len2 - 1 and ch != word2[j]:
                    # Means a graph edge
                    # 3.2. Optionally register node2 for ch2
                    ch2 = word2[j]
                    if ch2 not in nodes:
                        nodes.append(ch2)
                        adj_list.append([])

                    node2 = nodes.index(ch2)

                    # 3.3. Check if invalid
                    if node1 in adj_list[node2]:
                        return ""

                    # 3.4. Register edge
                    if node2 not in adj_list[node1]:
                        adj_list[node1].append(node2)

                    break

                elif j > len2 - 1:
                    break

        # Underspecified input 2
        if not nodes:
            abc_set = set()
            for w in words:
                for ch in w:
                    abc_set.union({ch})

            return "".join(abc_set)

        # Underspecified input 3
        if not adj_list or all(not l for l in adj_list):
            return "".join(nodes)

        visited = [False] * n
        # 4. Topological sort - need iterative
        q = [0]
        ordered = []
        path = set()
        while q:
            v = q[-1]  # item 1, just access, don't pop
            path = path.union({v})
            children = [x for x in adj_list[v] if x not in path]
            if not children:  # no child or all of them already visited
                ordered.insert(0, v)  # ordered = [v] + ordered
                q.pop()
            else:
                q.append(children[0])  # item 2, push just one child

        # 5. Construct abc
        abc = ""
        for v in ordered:
            abc += nodes[v]

        return abc
