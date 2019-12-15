def alien_order(words):
    # Underspecified input 0
    if not words:
        return []

    # Underspecified input 1
    if len(words) == 1:
        return "".join(sorted(set(list(words[0]))))

    nodes = []
    adj_list = []
    chars = set()

    # 1. Take each word pair
    for i, word1 in enumerate(words[:-1]):
        chars.union(set([ch for ch in word1]))
        len1 = len(word1)
        for j, word2 in enumerate(words[i:]):
            chars.union(set([ch for ch in word2]))
            len2 = len(word2)
            # 2. Find first character which differs
            for k in range(min(len1, len2)):
                ch1 = word1[k]
                # 3.1. Optionally register node1 for ch1
                if ch1 not in nodes:
                    nodes.append(ch1)
                    adj_list.append([])

                node1 = nodes.index(ch1)

                # 3.2. Optionally register node2 for ch2
                ch2 = word2[k]
                if ch2 not in nodes:
                    nodes.append(ch2)
                    adj_list.append([])

                node2 = nodes.index(ch2)

                if ch1 != ch2:
                    # Means a graph edge

                    # 3.3. Check if invalid (direct circle)
                    if node1 in adj_list[node2]:
                        return ""

                    # 3.4. Register edge
                    if node2 not in adj_list[node1]:
                        adj_list[node1].append(node2)

                    break

    left_out = chars - set(nodes)
    for ch in left_out:
        nodes.append(ch)
        adj_list.append([])

    n = len(nodes)

    # Underspecified input 2
    if not adj_list or all(not l for l in adj_list):
        return "".join(nodes)

    print(nodes, adj_list)
    order = [0] * n
    # 4. Topological sort - need iterative
    # 4.1 Find a good starting point for underspecified cases
    for start, ch in enumerate(nodes):
        if adj_list[start] and not order[start]:
            visited = [False] * n
            q = [(start, 1)]
            while q:
                v, level = q.pop()
                order[v] -= level
                for neighbor in adj_list[v]:
                    if not visited[neighbor]:
                        q.append((neighbor, level + 1))
                    else:
                        order[v] -= level

    # 5. Non involved (underspecified) charecters are de priotirized
    for i, o in enumerate(order):
        if not o:
            order[i] = -100000

    # 5. Construct abc
    zipped = zip(nodes, order)
    ordered = sorted(zipped, key=lambda x: -x[1])
    print(zipped, ordered)

    abc = ""
    for v in ordered:
        abc += v[0]

    return abc


import pytest


@pytest.mark.parametrize("words,expected", [
    (["zy", "zx"], "yxz"),
    (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    (["ac", "ab", "b"], "acb"),
])
def test_alien_dict(words, expected):
    assert(alien_order(words) == expected)


pytest.main()
