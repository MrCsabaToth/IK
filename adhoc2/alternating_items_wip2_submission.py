# Complete the function below.

def next_p(arr, l, x):
    while x <= l - 1 and arr[x] < 0:
        x += 1

    return x


def next_n(arr, l, x):
    while x < l - 1 and arr[x] >= 0:
        x += 1

    return x


def alternating_positives_and_negatives(arr):
    l = len(arr)
    n = next_n(arr, l, 0)
    p = next_p(arr, l, 0)

    i = 0
    while i < l and n < l and p < l:
        pos = i % 2 == 0
        if pos:
            if arr[i] < 0:
                # if only a swap needed, we can swap
                if p == n + 1:
                    arr[n], arr[p] = arr[p], arr[n]
                    n, p = p, n
                else:
                    arr.insert(i, arr[p])
                    del arr[p + 1]
                    n += 1

            p = next_p(arr, l, p + 1)
        else:
            if arr[i] >= 0:
                # if only a swap needed, we can swap
                if n == p + 1:
                    arr[n], arr[p] = arr[p], arr[n]
                    n, p = p, n
                else:
                    arr.insert(i, arr[n])
                    del arr[n + 1]
                    p += 1

            n = next_n(arr, l, n + 1)

        i += 1

    return arr

