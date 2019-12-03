def solve(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        seven = arr[start] % 2 == 0
        eeven = arr[end] % 2 == 0
        if seven:
            start += 1
        else:
            if eeven:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1

            end -= 1

    return arr
