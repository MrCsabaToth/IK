def findZeroSum(arr):
    length = len(arr)
    if length < 3:
        return []
    elif length == 3:
        if arr[0] + arr[1] + arr[2] == 0:
            return [",".join([str(s) for s in arr])]
        else:
            return []

    arr.sort()
    results = []

    table = dict()
    for item in arr:
        if item not in table:
            table[item] = 0
        else:
            table[item] += 1

    keys = list(table.keys())
    keys.sort()
    num_keys = len(keys)
    i = 0
    while i < num_keys:
        item = keys[i]
        j = i + 1 if table[item] < 2 else i
        while j < num_keys:
            item2 = keys[j]
            needed = -item - item2
            if needed in table:
                if needed == item2:
                    counter = 2 if item2 != item else 3
                    if table[needed] < counter:
                        continue

                if item + item2 + needed == 0:
                    sol = [item, item2, needed]
                    sol.sort()
                    solution = [str(s) for s in sol]
                    if solution not in results:
                        results.append(solution)

            j += 1

        i += 1

    return [",".join(r) for r in results]
