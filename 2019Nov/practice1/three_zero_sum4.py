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
    for i, num in enumerate(arr[:-2]):
        if i > 0 and num == arr[i - 1]:
            continue

        start = i + 1
        end = length - 1
        while start < end:
            balance = arr[start] + arr[end]
            if balance == -num:
                solution = [num, arr[start], arr[end]]
                results.append(solution)

                while start + 1 < end and arr[start] == arr[start + 1]:
                    start += 1

                while end - 1 > start and arr[end] == arr[end - 1]:
                    end -= 1

                start += 1
                end -= 1
            elif balance < -num:
                start += 1
            else:
                end -= 1

    return map(lambda x: ','.join([str(a) for a in x]), results)
