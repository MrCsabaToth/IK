def isPresent(arr, x):
    w = len(arr)
    h = len(arr[0])
    i = 0
    j = h - 1;
    while i <= w - 1 and j >= 0:
        if arr[i][j] == x:
            return "present"
        elif arr[i][j] < x:
            i += 1
        elif arr[i][j] > x:
            j -= 1

    return "not present"

