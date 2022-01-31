#
# Complete the 'merge_sort' function below.
#
# The function accepts an integer array as parameter.
#

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

    while i <= mid:
        # aux.append(arr[i])
        aux[k] = arr[i]
        i += 1
        k += 1
        
    while j <= end:
        # aux.append(arr[j])
        aux[k] = arr[j]
        j += 1
        k += 1

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

