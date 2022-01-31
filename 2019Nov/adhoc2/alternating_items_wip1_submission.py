# Complete the function below.

def find_next_pos(arr, l, x):
    while arr[x] < 0 and x < l - 1:
        x += 1

    return x


def find_next_neg(arr, l, x):
    while arr[x] >= 0 and x < l - 1:
        x += 1

    return x


def alternating_positives_and_negatives(arr):
    l = len(arr)
    n = find_next_neg(arr, l, 0)
    p = find_next_pos(arr, l, 0)

    i = 0
    while i < l:
        pos = i % 2 == 0
        if pos:
            if arr[i] >= 0:
                p = find_next_pos(arr, l, i + 1)
            else:
                # if only a swap needed, we can swap
                if p == n + 1:
                    arr[n], arr[p] = arr[p], arr[n]
                    n, p = p, n
                    p = find_next_pos(arr, l, p + 1)
                else:
                    arr.insert(i, arr[p])
                    del arr[p]
                    n += 1
                    p = find_next_pos(arr, l, p)
        else:
            if arr[i] < 0:
                p = find_next_pos(arr, l, i + 1)
            else:
                # if only a swap needed, we can swap
                if n == p + 1:
                    arr[n], arr[p] = arr[p], arr[n]
                    n, p = p, n
                    n = find_next_pos(arr, l, n + 1)
                else:
                    arr.insert(i, arr[n])
                    del arr[n]
                    p += 1
                    n = find_next_pos(arr, l, n)

        i += 1

    return arr
