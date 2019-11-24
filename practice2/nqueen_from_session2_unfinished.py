def find_all_arrangements(n):
    pre_res = dict()
    result = []

    def add_result(cols, rows):
        # print(cols, rows)
        coords = list(zip(cols, rows))
        coords.sort()
        sol_str = "".join(["{}_{}_".format(c[0], c[1]) for c in coords])
        if sol_str in pre_res:
            return

        pre_res[sol_str] = True
        solution = []
        for row in range(n):
            solution.append("".join([("q" if (col, row) in coords else "-") for col in range(n)]))

        result.append(solution)

    def nqueen_helper(cols, rows, colinv, rowinv, n):
        length = len(cols)
        if length:
            col = cols[length - 1]
            row = rows[length - 1]

        # Leaf node
        if length > 0:
            if any([(abs(cols[i] - col) == abs(rows[i] - row)) for i in range(length - 1)]):
                return

            if length == n:
                add_result(cols, rows)
                return

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
                    nqueen_helper(cols, rows, colinv, rowinv, n)
                    rowinv.append(j)
                    rows.pop()
                    colinv.append(i)
                    cols.pop()

    cols = []
    rows = []
    colinv = range(1, n + 1)
    rowinv = range(1, n + 1)
    return nqueen_helper(cols, rows, colinv, rowinv, n)
