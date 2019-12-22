# Complete the countWaysToClimb function below.
def countWaysToClimb(steps, n):
    steps = [step for step in steps if step <= n]
    dp = [0] * (n + 1)
    dp[0] = 1
    # for step in steps:
    #     if step <= n:
    #         dp[step] = 1

    for i in range(1, n + 1):
        count = 0
        for step in steps:
            if i - step >= 0:
                count += dp[i - step]
        dp[i] = count
        print(dp)

    return dp[n]


import pytest


@pytest.mark.parametrize("steps,n,expected", [
    ([1, 2, 3, 4, 5], 5, 25),
])
def test_edit_distance(steps, n, expected):
    assert(countWaysToClimb(steps, n) == expected)


pytest.main()
