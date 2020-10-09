#
# Complete the getMergedIntervals function below.
#
def getMergedIntervals(inputArray):
    if len(inputArray) <= 1:
        return inputArray

    inputArray.sort(key=lambda x: x[0])
    stack = [inputArray[0]]

    i = 1
    while i < len(inputArray):
        domain = inputArray[i]
        if domain[0] <= stack[-1][1] and domain[1] > stack[-1][1]:
            stack[-1][1] = max(stack[-1][1], domain[1])
        elif domain[0] > stack[-1][1]:
            stack.append(domain)
        i += 1

    return stack
