#
# Complete the getMergedIntervals function below.
#
def getMergedIntervals(inputArray):
    if len(inputArray) <= 1:
        return inputArray

    inputArray.sort(key=lambda x: x[0])
    marker = 0

    i = 1
    while i < len(inputArray):
        domain = inputArray[i]
        if domain[0] <= inputArray[marker][1] and domain[1] > inputArray[marker][1]:
            inputArray[marker][1] = max(inputArray[marker][1], domain[1])
        elif domain[0] > inputArray[marker][1]:
            marker += 1
            inputArray[marker] = inputArray[i]
        i += 1

    marker += 1
    return inputArray[:marker]
