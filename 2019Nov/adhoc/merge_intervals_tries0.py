#
# Complete the getMergedIntervals function below.
#
def getMergedIntervals(inputArray):
    if len(inputArray) <= 2:
        return inputArray

    inputArray.sort(key=lambda x: x[0])
    stack = [inputArray[0]]
    inputArray = inputArray[1:]

    while len(inputArray) > 0:
        domain = inputArray[0]
        if (domain[0] <= stack[-1][0] <= domain[1] or domain[0] <= stack[-1][1] <= domain[1] or
            stack[-1][0] < domain[0] and stack[-1][1] > domain[1] or
            domain[0] < stack[-1][0] and domain[1] > stack[-1][1]):
            pool[i] = [min(stack[-1][0], domain[0]), max(stack[-1][1], domain[1])]
        else:
            pool.append(domain)
            i = 0
        inputArray = inputArray[1:]

    return inputArray
