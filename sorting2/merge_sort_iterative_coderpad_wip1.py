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
    j = mid
    k = 0
    print(length, i, j, mid)
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
    while run < length:
        beg = 0
        while beg < length:
            merge_helper(arr, beg, min(beg + run - 1, length - 1))
            beg += run

        run *= 2

    return arr


import pytest


# @pytest.mark.parametrize("i", range(30))
def test_merge_sort():
    # rng = random.SystemRandom()
    #length = rng.randint(10, 40)
    # a = [rng.randint(0, 1000) for j in range(length)]
    a = [0, 1, 3, 2]
    a2 = sorted(a)
    # print(length, k)
    merge_sort(a)
    for j in range(len(a)):
        assert a[j] == a2[j]


pytest.main()
