def numberOfPaths(matrix):
    n = len(matrix)
    if not n:
        return 0

    m = len(matrix[0])
    if not m:
        return 0

    dp = [None] * n
    for i in range(n):
        dp[i] = [0] * m

    if not matrix[0][0] or not matrix[n - 1][m - 1]:
        return 0

    dp[0][0] = 1
    # 1. Initialize first row
    for j in range(1, m):
        dp[0][j] =  matrix[0][j] if dp[0][j - 1] else 0

    if n == 1:
        return dp[0][m - 1]

    # 2. Initialize first column
    for i in range(1, n):
        dp[i][0] = matrix[i][0] if dp[i - 1][0] else 0

    if m == 1:
        return matrix[n - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    modulo = 10**9 + 7
    return dp[n - 1][m - 1] % modulo


import pytest


@pytest.mark.parametrize("matrix,expected", [
    ([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ], 2),
    ([
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ], 4),
    ([
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
    ], 3),
    ([
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ], 5),
    ([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ], 11),
])
def test_numberOfPaths(matrix, expected):
    assert(numberOfPaths(matrix) == expected)


pytest.main()
