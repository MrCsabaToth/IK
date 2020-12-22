def merge_helper(arr, beg, end, mid, aux):
    length = end - beg + 1
    if length <= 1:
        return

    if length == 2:
        if arr[beg] > arr[end]:
            arr[beg], arr[end] = arr[end], arr[beg]

        return

    i = beg
    j = mid
    mid -= 1
    k = beg
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            aux[k] = arr[i]
            i += 1
        else:
            aux[k] = arr[j]
            j += 1

        k += 1

    while i <= mid:
        aux[k] = arr[i]
        i += 1
        k += 1

    while j <= end:
        aux[k] = arr[j]
        j += 1
        k += 1

    k = beg
    while k <= end:
        arr[k] = aux[k]
        k += 1


def merge_sort(arr):
    length = len(arr)
    aux = [0] * length
    run = 2
    while run <= length:
        beg = 0
        residual = length % run
        while beg < length:
            end = beg + run - 1
            mid = beg + run // 2
            merge_helper(arr, beg, min(end, length - 1), mid, aux)
            if residual != 0 and beg + 2 * run > length:
                end = length - 1
                mid += run // 2
                merge_helper(arr, beg, min(end, length - 1), mid, aux)
                break

            beg += run

        run *= 2

    return arr


import random
import pytest


@pytest.mark.parametrize("i", range(100))
def test_merge_sort(i):
    rng = random.SystemRandom()
    length = rng.randint(3, 30)
    a = [rng.randint(0, 100) for j in range(length)]
    a2 = sorted(a)
    merge_sort(a)
    for j in range(len(a)):
        assert a[j] == a2[j]


pytest.main()

