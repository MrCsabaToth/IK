# Complete the countWaysToClimb function below.
def countWaysToClimb(steps, n):
    steps = [step for step in steps if step <= n]
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        count = 0
        for step in steps:
            if i - step >= 0:
                count += dp[i - step]
        dp[i] = count

    return dp[n]
