#
# Complete the 'merge_sort' function below.
#
# The function accepts an integer array as parameter.
#

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
    while i < mid and j <= end:
        if arr[i] < arr[j]:
            # aux.append(arr[i])
            aux[k] = arr[i]
            i += 1
        else:
            # aux.append(arr[j])
            aux[k] = arr[j]
            j += 1

        k += 1

    while i < mid:
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
        while beg < length:
            merge_helper(arr, beg, min(beg + run - 1, length - 1))
            beg += run

        run *= 2

    return arr
