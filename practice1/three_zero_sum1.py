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
    i = 0
    while i < length:
        target = -arr[i]
        start = i + 1
        end = length - 1
        while start < end:
            balance = arr[start] + arr[end]
            if balance == target:
                sol = [arr[i], arr[start], arr[end]]
                sol.sort()
                solution = [str(s) for s in sol]
                if solution not in results:
                    results.append(solution)

                start += 1
                end -= 1
            elif balance < target:
                start += 1
            else:
                end -= 1

        i += 1

    return [",".join(r) for r in results]
