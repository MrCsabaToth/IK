def merge_helper(arr, beg, end, mid):
    length = end - beg + 1
    if length <= 1:
        return

    if length == 2:
        if arr[beg] > arr[end]:
            arr[beg], arr[end] = arr[end], arr[beg]
        return

    aux = [0] * length
    # aux = []
    i = beg
    j = mid
    mid -= 1
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
        print("run ", run)
        beg = 0
        residual = length % run
        while beg < length:
            end = beg + run - 1
            mid = beg + run // 2
            merge_helper(arr, beg, min(end, length - 1), mid)
            if residual != 0 and beg + 2 * run > length:
                end = length - 1
                mid += run // 2
                merge_helper(arr, beg, min(end, length - 1), mid)
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
    print(length)
    a = [rng.randint(0, 100) for j in range(length)]
    # a = [0, 1, 3, 2]
    # a = [0, 3, 2, 1]
    # a = [1, 2, 3, 2, 1]
    # a = [26, 81, 4, 16, 2, 56]
    a2 = sorted(a)
    print(a)
    merge_sort(a)
    for j in range(len(a)):
        assert a[j] == a2[j]


pytest.main()
