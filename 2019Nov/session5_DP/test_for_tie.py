def Test_for_tie(weights):
    allsum = sum(weights)
    def test_for_tie_helper(weights, i, remaining, gr1sum, gr2sum):
        if remaining == 0:
            return gr1sum == gr2sum

        # Backtrack
        if abs(gr1sum - gr2sum) > remaining:
            return False

        if test_for_tie_helper(weights, i + 1, remaining - weights[i], gr1sum + weights[i], gr2sum):
            return True

        return test_for_tie_helper(weights, i + 1, remaining - weights[i], gr1sum, gr2sum + weights[i])

    return test_for_tie_helper(weights, 0, allsum, 0, 0)


def Test_for_tie2(weights):
    allsum = sum(weights)
    length = len(weights)
    if allsum % 2 == 1:
        return False

    def test_for_tie_helper(weights, i, remaining):
        if remaining == 0:
            return True

        # Stopping
        if i == length:
            return False

        # Backtracking
        if remaining < 0:
            return False

        if test_for_tie_helper(weights, i + 1, remaining - weights[i]):
            return True

        return test_for_tie_helper(weights, i + 1, remaining)

    return test_for_tie_helper(weights, 0, allsum // 2)


def Test_for_tie2_memoize(weights):
    allsum = sum(weights)
    length = len(weights)
    if allsum % 2 == 1:
        return False

    memo = dict()
    def test_for_tie_helper(weights, i, remaining):
        if remaining == 0:
            return True

        key = "{}_{}".format(i, remaining)
        if key in memo:
            return memo[key]

        # Stopping
        if i == length:
            memo[key] = False
            return False

        # Backtracking
        if remaining < 0:
            memo[key] = False
            return False

        if test_for_tie_helper(weights, i + 1, remaining - weights[i]):
            memo[key] = True
            return True

        result = test_for_tie_helper(weights, i + 1, remaining)
        memo[key] = result
        return result


    return test_for_tie_helper(weights, 0, allsum // 2)


def Test_for_tie2_iterative(weights):
    allsum = sum(weights)
    if allsum % 2 == 1:
        return False

    halfsum = allsum // 2
    length = len(weights)
    dp = [None] * (halfsum + 1)
    for i, _ in enumerate(dp):
        dp[i] = [None] * (length + 1)

    for i in range(length + 1):
        dp[0][i] = True

    for j in range(1, halfsum + 1):
        dp[j][length] = False

    for summ in range(1, halfsum + 1):
        for i in range(length - 1, -1, -1):
            result = False
            if summ >= weights[i]:
                result = dp[summ - weights[i]][i + 1]

            dp[summ][i] = result or dp[summ][i + 1]

    # for k in range(halfsum + 1):
    #     print(dp[k])
    return dp[halfsum][0]


# def Test_for_tie2_iterative_tracking(weights):
#     allsum = sum(weights)
#     if allsum % 2 == 1:
#         return False

#     halfsum = allsum // 2
#     length = len(weights)
#     dp = [None] * (halfsum + 1)
#     for i, _ in enumerate(dp):
#         dp[i] = [(None, None)] * (length + 1)

#     for i in range(length + 1):
#         dp[0][i] = (True, ?)

#     for j in range(1, halfsum + 1):
#         dp[j][length] = (False, ?)

#     for summ in range(1, halfsum + 1):
#         for i in range(length - 1, -1, -1):
#             result = False
#             if summ >= weights[i]:
#                 result = dp[summ - weights[i]][i + 1]

#             dp[summ][i] = result or dp[summ][i + 1]

#     # for k in range(halfsum + 1):
#     #     print(dp[k])
#     return dp[halfsum][0]


import pytest


@pytest.mark.parametrize("weights,expected", [
    ([1, 2, 3, 4, 5, 7], True),
    ([1, 2, 3, 4, 5, 8], False),
])
def test_test_for_tie(weights, expected):
    assert(Test_for_tie(weights) == expected)
    assert(Test_for_tie2(weights) == expected)
    assert(Test_for_tie2_memoize(weights) == expected)
    assert(Test_for_tie2_iterative(weights) == expected)


pytest.main()
