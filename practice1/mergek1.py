def mergeArrays(arr):
    k = len(arr)
    n = len(arr[0])

    # Step 1: determine if it's ascending or descending
    # Any array could be just a series fo same values
    # so look until we find a different value
    ascending = True
    if n > 1:
        for i in range(k):
            if arr[i][n - 1] < arr[i][n - 2]:
                ascending = False
                break

    nk = n * k
    indexes = [0] * k
    res = [0] * nk
    out_index = 0
    while out_index < nk:
        # Step 2: Determine the next value to append
        next_value = None
        for i in range(k):
            if indexes[i] < n:
                item_i = arr[i][indexes[i]]
                if (
                    next_value is None or
                    ascending and item_i < next_value or
                    not ascending and item_i > next_value
                ):
                    next_value = item_i

        # Step 3: append, possibly also multiple values if repeated
        for i in range(k):
            if indexes[i] < n:
                while indexes[i] < n and out_index < nk and arr[i][indexes[i]] == next_value:
                    res[out_index] = next_value
                    out_index += 1
                    # res.append(next_value)
                    indexes[i] += 1

    return res
