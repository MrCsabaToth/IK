def findZeroSum(arr):
    length = len(arr)
    if length < 3:
        return []
    elif length == 3:
        if arr[0] + arr[1] + arr[2] == 0:
            return [",".join([str(s) for s in arr])]
        else:
            return []

    results = []

    table = dict()
    for item in arr:
        if item not in table:
            table[item] = 1
        else:
            table[item] += 1

    # print(table)
    # keys = list(table.keys())
    # keys.sort()
    # num_keys = len(keys)
    # print(num_keys, keys)
    # i = 0
    # while i < num_keys:
    #     item = keys[i]
    #     j = i if table[item] >= 2 else i + 1
    #     # print(i, j)
    #     for item2 in keys[j:]:
    #         needed = -(item + item2)
    #         if needed in table:
    #             if needed == item2:
    #                 counter = 2 if item2 != item else 3
    #                 if table[needed] < counter:
    #                     continue
    #             elif needed == item:
    #                 if table[needed] < 2:
    #                     continue

    #             sol = [item, item2, needed]
    #             sol.sort()
    #             solution = [str(s) for s in sol]
    #             if solution not in results:
    #                 results.append(solution)

    #     i += 1

    keys = table.keys()
    for item in keys:
        for item2 in keys:
            needed = -(item + item2)
            if needed in table:
                if needed == item2:
                    counter = 2 if item2 != item else 3
                    if table[needed] < counter:
                        continue
                elif needed == item:
                    if table[needed] < 2:
                        continue

                sol = [item, item2, needed]
                sol.sort()
                solution = [str(s) for s in sol]
                if solution not in results:
                    results.append(solution)

    return [",".join(r) for r in results]
