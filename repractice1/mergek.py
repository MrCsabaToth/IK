import heapq

def mergeArrays(arr):
    k = len(arr)
    if k == 0:
        return []

    n = len(arr[0])
    if n == 0:
        return []

    ascending = True
    for i in range(k):
        if arr[i][0] > arr[i][n - 1]:
            ascending = False
            break

    ret = arr[0][:] if ascending else [-x for x in arr[0][::-1]]
    heapq.heapify(ret)
    for i in range(1, k):
        for j in range(n):
            heapq.heappush(ret, arr[i][j] if ascending else -arr[i][j])

    return [(heapq.heappop(ret) if ascending else -heapq.heappop(ret)) for _ in range(k * n)]


import pytest


def test_flag():
    arr = [
      [34, 26, 20, 13, 11, 7, 4, 4],
      [41, 34, 27, 23, 19, 10, 8, 0],
      [26, 25, 19, 12, 7, 7, 7, 5],
      [46, 39, 35, 33, 27, 19, 12, 9],
      [33, 24, 22, 18, 18, 10, 3, 0],
      [42, 35, 35, 30, 21, 20, 12, 9],
      [42, 33, 24, 21, 12, 12, 8, 7],
      [29, 23, 21, 18, 18, 11, 8, 7],
      [35, 30, 30, 23, 15, 14, 8, 7],
      [20, 18, 17, 16, 12, 11, 5, 4],
    ]

    output = arr[0][:]
    for i in range(1, len(arr)):
        output.extend(arr[i][:])

    result = mergeArrays(arr)
    assert result == sorted(output, reverse=True)


pytest.main()
