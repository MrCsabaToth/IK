def find_minimum(arr):
    if not arr:
        return None
    n = len(arr)
    max_i = n - 1
    if n == 1:
        return arr[0]
    elif n == 2:
        return min(arr[0], arr[1])
    elif n == 3:
        return min(arr[0], arr[1], arr[2])
    elif arr[0] - arr[max_i] < 0 and arr[0] - arr[1] < 0 and arr[n - 2] - arr[max_i] < 0:
        return arr[0]
    elif arr[0] - arr[max_i] > 0 and arr[0] - arr[1] > 0 and arr[n - 2] - arr[max_i] > 0:
        return arr[max_i]

    asc = arr[0] - arr[max_i] > 0
    b = 0
    e = max_i
    while b <= e:
        if arr[b] - arr[e] <= 0 and asc:
            return arr[b]
        elif arr[b] - arr[e] >= 0 and not asc:
            return arr[e]

        m = (b + e) // 2
        if asc:
            if arr[m] - arr[b] >= 0:
                # Minimum is in right subarray
                b = m + 1;
            else:
                # Minimum is in left subarray 
                e = m
        else:
            if arr[m] - arr[b] < 0:
                # Minimum is in right subarray
                b = m
            else:
                # Minimum is in left subarray
                e = m

    return min(arr[b], arr[e], arr[m])

