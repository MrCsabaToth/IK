def findZeroSum(arr):
    sol_cache = dict()
    solutions = []

    if not arr:
        return solutions

    lookup = dict()
    for i, a in enumerate(arr):
        if a not in lookup:
            lookup[a] = 1
        else:
            lookup[a] += 1

    for i, ai in enumerate(arr):
        for j, aj in enumerate(arr):
            if i == j:
                continue

            part = -ai - aj
            if part in lookup:
                count = 1
                if part == ai:
                    count += 1

                if part == aj:
                    count += 1

                if count <= lookup[part]:
                    solution_str = ",".join([str(a) for a in sorted([ai, aj, part])])
                    if solution_str not in sol_cache:
                        sol_cache[solution_str] = True
                        solutions.append(solution_str)

    return solutions
