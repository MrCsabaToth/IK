import heapq

def mergeArrays(arr):
    k = len(arr)
    n = len(arr[0])

    # Step 1: determine if it's ascending or descending
    # Any array could be just a series fo same values
    # so look until we find a different value
    ascending = True
    if n > 1:
        for i in range(k):
            if arr[i][n - 1] < arr[i][0]:
                ascending = False
                break

    range_k = range(k)
    for i in range_k[1:]:
        arr[0].extend(arr[i])

    heapq.heapify(arr[0])
    nk = n * k
    res = [1000000] * nk

    out_index = 0 if ascending else nk - 1
    while ascending and out_index < nk or not ascending and out_index >= 0:
        res[out_index] = heapq.heappop(arr[0])
        if ascending:
            out_index += 1
        else:
            out_index -= 1

    return res
