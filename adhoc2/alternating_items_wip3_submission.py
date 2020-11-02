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
    res = []

    i = 0
    while i < l and n < l and p < l:
        pos = i % 2 == 0

        if pos:
            res.append(arr[p])
            p += 1
            p = next_p(arr, l, p)
        else:
            res.append(arr[n])
            n += 1
            n = next_n(arr, l, n)

        i += 1

    while n < l:
        if arr[n] < 0:
            res.append(arr[n])
        n += 1

    while p < l:
        if arr[p] >= 0:
            res.append(arr[p])
        p += 1

    return res
