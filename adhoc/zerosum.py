# Complete the sumZero function below.
def sumZero(arr):
    solutions = []
    lookup = {0: -1}
    summ = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            return [i, i]
        #if arr[i] == -summ:
        #    return [0, i]

        summ += arr[i]
        if summ in lookup.keys():
            return [lookup[summ] + 1, i]
        else:
            lookup[summ] = i

    return [-1]

