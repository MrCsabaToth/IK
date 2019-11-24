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

    def q_helper(cols, rows, scol, srow, level):
        length = len(scol)
        if length > 0:
            col = scol[length - 1]
            row = srow[length - 1]
            if any([(abs(scol[i] - col) == abs(srow[i] - row)) for i in range(length - 1)]):
                return

            if not len(cols):  # or not level:
                # print(scol, srow, cols, rows)
                add_result(scol, srow)
                return

        cols_copy = cols.copy()
        rows_copy = rows.copy()

        for c in cols_copy:
            cols.remove(c)
            scol.append(c)

            for r in rows_copy:
                rows.remove(r)
                srow.append(r)
                q_helper(cols, rows, scol, srow, level - 1)
                srow.pop()
                rows.append(r)

            scol.pop()
            cols.append(c)

    cols0 = list(range(n))  # problem snippet columns part
    rows0 = list(range(n))  # problem snippet rows part
    scol0 = []  # solution columns part
    srow0 = []  # solution rows part
    q_helper(cols0, rows0, scol0, srow0, n)

    return result
