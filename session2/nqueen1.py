def nqueen_helper(cols, rows, colinv, rowinv, n):
    # Leaf node
    if len(cols) == n:
        sol = sorted(["({}x{})".format(pos[0], pos[1]) for pos in zip(cols, rows)])
        return set(sol)

    result = set()
    # Internal node
    for i in colinv[:]:
        for j in rowinv[:]:
            attack = False
            for k in range(len(cols)):
                dcol = abs(i - cols[k])
                drow = abs(j - rows[k])
                if dcol == drow:
                    attack = True
                    break

            if not attack:
                cols.append(i)
                colinv.remove(i)
                rows.append(j)
                rowinv.remove(j)
                result = result.union(nqueen_helper(cols, rows, colinv, rowinv, n))
                rowinv.append(j)
                rows.pop()
                colinv.append(i)
                cols.pop()

    return result


def nqueen(n):
    cols = []
    rows = []
    colinv = range(1, n + 1)
    rowinv = range(1, n + 1)
    return nqueen_helper(cols, rows, colinv, rowinv, n)
