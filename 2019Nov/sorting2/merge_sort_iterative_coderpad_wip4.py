def merge_helper(arr, beg, end):
    length = end - beg + 1
    if length <= 1:
        return

    if length == 2:
        if arr[beg] > arr[end]:
            arr[beg], arr[end] = arr[end], arr[beg]
        return

    aux = [0] * length
    # aux = []
    mid = (beg + end) // 2
    i = beg
    j = mid + 1
    k = 0
    print(length, i, j, mid, beg, end, arr)
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            # aux.append(arr[i])
            aux[k] = arr[i]
            i += 1
        else:
            # aux.append(arr[j])
            aux[k] = arr[j]
            j += 1

        k += 1

    print(i, j, k, mid, aux)
    while i <= mid:
        # aux.append(arr[i])
        aux[k] = arr[i]
        i += 1
        k += 1

    print(i, j, k, mid, aux)
    while j <= end:
        # aux.append(arr[j])
        aux[k] = arr[j]
        j += 1
        k += 1

    print(beg, end, aux)
    # arr[beg:end] = aux
    a = beg
    for elem in aux:
        arr[a] = elem
        a += 1


def merge_sort(arr):
    length = len(arr)
    run = 2
    while run <= length:
        beg = 0
        residual = length % run
        while beg < length:
            merge_helper(arr, beg, min(beg + run - 1, length - 1))
            if residual != 0 and beg + 2 * run > length:
                merge_helper(arr, length - 1 - 2 * residual, length - 1)
            beg += run

        run *= 2

    return arr


import random
import pytest


@pytest.mark.parametrize("i", range(1))
def test_merge_sort(i):
    rng = random.SystemRandom()
    length = rng.randint(3, 6)
    # a = [rng.randint(0, 100) for j in range(length)]
    # a = [0, 1, 3, 2]
    # a = [0, 3, 2, 1]
    # a = [1, 2, 3, 2, 1]
    a = [26, 81, 4, 16, 2, 56]
    a = [44, 81, 62, 45, 54, 13]
    a = [86, 88, 91, 80, 6, 94]
    a = [39, 62, 32, 66, 25, 10]
    a = [70, 56, 56, 61, 59, 39]
    a = [32, 82, 43, 59, 22, 62]
    a = [49, 73, 35, 46, 45, 18]
    a = [70, 87, 17, 18, 64, 1]
    a2 = sorted(a)
    print(length, a)
    merge_sort(a)
    for j in range(len(a)):
        assert a[j] == a2[j]


pytest.main()

