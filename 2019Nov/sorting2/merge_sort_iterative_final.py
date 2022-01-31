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
    # Bulk of merge
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            aux[k] = arr[i]
            i += 1
        else:
            aux[k] = arr[j]
            j += 1

        k += 1

    # Continue merge of leftovers 1
    while i <= mid:
        aux[k] = arr[i]
        i += 1
        k += 1

    # Continue merge of leftovers 2
    while j <= end:
        aux[k] = arr[j]
        j += 1
        k += 1

    # Shovel from aux merge array back to the array
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
