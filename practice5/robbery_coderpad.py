# Complete the maxStolenValue function below.
def maxStolenValue(values):
    length = len(values)
    dp = [0] * (length + 1)

    for i in range(1, length + 1):
        subordinates = [dp[i] for i in range(i - 1)]
        dp[i] = values[i - 1] + (max(subordinates) if subordinates else 0)
        print(i, dp)

    return dp[length]


import pytest


@pytest.mark.parametrize("values,expected", [
    ([6, 1, 2, 7], 13),
])
def test_edit_distance(values, expected):
    assert(maxStolenValue(values) == expected)


pytest.main()
