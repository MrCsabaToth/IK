import heapq

def mergeArrays(arr):
    if not arr or not arr[0]:
        return []

    k = len(arr)
    n = len(arr[0])
    ascending = True
    for ar in arr:
        if ar[0] > ar[n - 1]:
            ascending = False
            break

    extended = [None] * (k * n)
    for i, ar in enumerate(arr):
        for j, elem in enumerate(ar):
            extended[i * n + j] = elem if ascending else -elem

    heapq.heapify(extended)
    merged = [None] * (k * n)
    idx = 0
    while extended:
        elem = heapq.heappop(extended)
        merged[idx] = elem if ascending else -elem
        idx += 1

    return merged
