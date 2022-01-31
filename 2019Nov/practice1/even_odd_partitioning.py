def solve(arr):
    length = len(arr)
    start = 0
    end = length - 1
    while start < end:
        start_even = arr[start] % 2 == 0
        end_even = arr[end] % 2 == 0
        if not start_even:
            if end_even:
                (arr[start], arr[end]) = (arr[end], arr[start])
                start += 1

            end -= 1
        else:  # start_even
            start += 1
            if not end_even:
                end -= 1

    return arr
