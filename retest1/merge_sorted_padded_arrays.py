def merger_first_into_second(arr1, arr2):
    p1 = len(arr1) - 1
    runner = len(arr2) - 1
    # Assuming arr2 is the padded
    p2 = len(arr2) - len(arr1) - 1

    while p1 >= 0 or p2 >= 0 and p1 != runner and p2 != runner:
        if p1 >= 0 and p2 >= 0:
            if arr1[p1] > arr2[p2]:
                arr2[runner] = arr1[p1]
                p1 -= 1
            else:
                arr2[runner] = arr2[p2]
                p2 -= 1
        elif p1 >= 0:
            arr2[runner] = arr1[p1]
            p1 -= 1
        else:
            arr2[runner] = arr2[p2]
            p2 -= 1

        runner -= 1
