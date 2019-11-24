def find_all_arrangements(n):
    pre_res = dict()
    result = []
    diagf = [False] * (2 * n -1)  # forward diagonal
    diagb = [False] * (2 * n -1)  # backward diagonal

    def add_result(cols, rows):
        solution = []
        for row in range(n):
            idx = rows.index(row)
            col_idx = cols[idx]
            solution.append("".join([("q" if i == col_idx else "-") for i in range(n)]))

        sol_str = "".join(solution)
        if sol_str in pre_res:
            return

        pre_res[sol_str] = True
        result.append(solution)

    def q_helper(cols, rows, scol, srow):
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
                if not diagf[c + r] and not diagb[c - r + n - 1]:
                    rows.remove(r)
                    srow.append(r)
                    diagf[c + r] = True
                    diagb[c - r + n - 1] = True
    
                    q_helper(cols, rows, scol, srow)
    
                    diagb[c - r + n - 1] = False
                    diagf[c + r] = False
                    srow.pop()
                    rows.append(r)

            scol.pop()
            cols.append(c)

    cols0 = list(range(n))  # problem snippet columns part
    rows0 = list(range(n))  # problem snippet rows part
    scol0 = []  # solution columns part
    srow0 = []  # solution rows part
    q_helper(cols0, rows0, scol0, srow0)

    return result
    