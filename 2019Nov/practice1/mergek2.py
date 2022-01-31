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
    res = [1000000] * nk
    out_index = 0
    range_k = range(k)
    while out_index < nk:
        # Step 2: Determine the next value to append
        lead_values = [arr[i][indexes[i]] for i in range_k if indexes[i] < n]
        next_value = min(lead_values) if ascending else max(lead_values)

        # Step 3: append, possibly also multiple values if repeated
        i = 0
        while i < k:
            while indexes[i] < n and out_index < nk and arr[i][indexes[i]] == next_value:
                res[out_index] = next_value
                out_index += 1
                # res.append(next_value)
                indexes[i] += 1

            i+= 1

    return res
