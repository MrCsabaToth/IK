#
#Complete the fumction numberOfPaths
#The fumction takes integers 2D integer array, matrix, as parameter.
#
def numberOfPaths(matrix):
    n = len(matrix)
    if not n:
        return 0

    m = len(matrix[0])
    if not m:
        return 0

    if not matrix[0][0] or not matrix[n - 1][m - 1]:
        return 0

    for j in range(1, m):
        matrix[0][j] = matrix[0][j] if matrix[0][j - 1] else 0

    if n == 1:
        return matrix[0][m - 1]

    for i in range(1, n):
        matrix[i][0] = matrix[i][0] if matrix[i - 1][0] else 0

    if m == 1:
        return matrix[n - 1][0]

    # We override the matrix, it serves as our DP array
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j]:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    modulo = 10**9 + 7
    return matrix[n - 1][m - 1] % modulo
