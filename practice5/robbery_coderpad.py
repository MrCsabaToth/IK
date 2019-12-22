# Complete the maxStolenValue function below.
def maxStolenValue(values):
    length = len(values)
    dp = [0] * (length + 1)
    dp[1] = values[0]

    for i in range(2, length + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + values[i - 1])

    return dp[length]


import pytest


@pytest.mark.parametrize("values,expected", [
    ([6, 1, 2, 7], 13),
])
def test_edit_distance(values, expected):
    assert(maxStolenValue(values) == expected)


pytest.main()
