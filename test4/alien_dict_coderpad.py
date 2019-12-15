def alien_order(words):
    # Underspecified input 0
    if not words:
        return []

    # Underspecified input 1
    if len(words) == 1:
        return "".join(sorted(set(list(words[0]))))

    nodes = []
    adj_list = []

    # 1. Take each word pair
    for i, word1 in enumerate(words[:-1]):
        len1 = len(word1)
        for j, word2 in enumerate(words[i:]):
            len2 = len(word2)
            # 2. Find first character which differs
            different = False
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

                if ch1 != ch2 and not different:
                    # Means a graph edge

                    # 3.3. Check if invalid (direct circle)
                    if node1 in adj_list[node2]:
                        return ""

                    # 3.4. Register edge
                    if node2 not in adj_list[node1]:
                        adj_list[node1].append(node2)

                    different = True
            
            if k < len2:
                for ch in word2[k:]:
                    if not ch in nodes:
                        nodes.append(ch)
                        adj_list.append([])

    for ch in words[0]:
        if not ch in nodes:
            nodes.append(ch)
            adj_list.append([])

    # Underspecified input 2
    if not adj_list or all(not l for l in adj_list):
        return "".join(nodes)

    # 4. Topological sort - need iterative
    # 4.1 Find a good starting point for underspecified cases
    for start, ch in enumerate(nodes):
        if adj_list[start]:
            break

    visited = [False] * len(nodes)
    q = [start]
    ordered = []
    while q:
        v = q[-1]  # item 1, just access, don't pop
        visited[v] = True
        children = [x for x in adj_list[v] if not visited[x]]
        if not children:  # no child or all of them already visited
            ordered.insert(0, v)  # ordered = [v] + ordered
            q.pop()
        else:
            q.append(children[0])  # item 2, push just one child

    # 5. Construct abc
    visited = [False] * len(nodes)
    abc = ""
    for v in ordered:
        abc += nodes[v]
        visited[v] = True

    for i, indicator in enumerate(visited):
        if not indicator:
            abc += nodes[i]

    return abc


import pytest


@pytest.mark.parametrize("words,expected", [
    (["zy", "zx"], "yxz"),
    (["wrt","wrf","er","ett","rftt"], "wertf"),
])
def test_alien_dict(words, expected):
    assert(alien_order(words) == expected)


pytest.main()
