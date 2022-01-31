#
#Complete the fumction numberOfPaths
#The fumction takes integers 2D integer array, matrix, as parameter.
#
def numberOfPaths(matrix):
    n = len(matrix)
    if not n:
        return 0

    if n == 1:
        return 1 if all([cell for cell in matrix[0]]) else 0

    m = len(matrix[0])
    if m == 1:
        return 1 if all([matrix[i][0] for i in range(n)]) else 0

    if not matrix[0][0]:
        return 0

    # We override the matrix, it serves as our DP array
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j]:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[n - 1][m - 1]
