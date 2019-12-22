def minimum_coins(coins, value):
    dp = [0] * (value + 1)

    for i in range(1, value + 1):
        min_count = None
        dp[i] = 1 + min([dp[i - coin] for coin in coins if i - coin >= 0]) 

    return dp[value]
