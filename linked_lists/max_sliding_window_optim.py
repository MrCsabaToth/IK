def log_search(arr, val, find):
    if not arr:
        return -1 if find else 0

    if not find and val > arr[-1]:
        return len(arr)

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            i = mid
            while i >= 0 and arr[i] == val:
                i -= 1

            return i + 1
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    if find:
        return -1

    return min(low, high)


def max_in_sliding_window(arr, w):
    win = sorted(arr[:w])
    rlen = len(arr) - w + 1
    ret = [None] * rlen
    m = win[-1]
    ret[0] = m
    for i in range(rlen - 1):
        out = arr[i]
        pos1 = log_search(win, out, True)
        if pos1 >= 0:
            win = win[:pos1] + win[pos1 + 1:]

        inp = arr[w + i]
        pos2 = log_search(win, inp, False)
        win = [inp] + win[pos2+1:]
        m = win[-1]
        ret[i + 1] = m

    return ret
