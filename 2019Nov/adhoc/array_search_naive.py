def isPresent(arr, x):
    w = len(arr)
    h = len(arr[0])
    i = 0
    j = 0
    while i < w and j < h:
        j = 0
        while j < h and arr[i][j] <= x:
            if arr[i][j] == x:
                return "present"
            j += 1

        if j >= h:
            j = 0
        i += 1

    return "present" if i < w and j < h and arr[i][j] == x else "not present"

