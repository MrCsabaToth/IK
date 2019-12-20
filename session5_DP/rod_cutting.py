def rod_cutting_recursive_6way1(prices):
    def cut_helper(prices, remaining, partial):
        if remaining == 0:
            return partial + prices[0]

        best = 0
        for i in range(1, remaining + 1):
            round_i = cut_helper(prices, remaining - i, partial + prices[i])
            if round_i > best:
                best = round_i

        return best

    return cut_helper(prices, 6, 0)


def rod_cutting_recursive_6way2_memoize(prices):
    memo = dict()
    def cut_helper(remaining):
        if remaining == 0:
            return 0

        if remaining in memo:
            return memo[remaining]

        best = 0
        for i in range(1, remaining + 1):
            round_i = prices[i] + cut_helper(remaining - i)

            if round_i > best:
                best = round_i

        memo[remaining] = best
        return best

    return cut_helper(6)


def rod_cutting_recursive_6way2(prices):
    def cut_helper(remaining):
        if remaining == 0:
            return 0

        best = 0
        for i in range(1, remaining + 1):
            round_i = prices[i] + cut_helper(remaining - i)
            if round_i > best:
                best = round_i

        return best

    return cut_helper(6)


def rod_cutting_iterative_6way(prices):
    n = len(prices)
    cache = [0] * (n + 1)
    for runner in range(1, n + 1):
        best = 0
        back = min(n, runner)
        for i in range(1, back):
            partial = prices[i] + cache[runner - i]
            if partial > best:
                best = partial

        cache[runner] = best

    return cache[n]


def rod_cutting_recursive_2way1(prices):
    def cut_helper(prices, remaining, partial):
        if remaining == 0:
            return partial + prices[0]

        best = 0
        for i in range(1, remaining + 1):
            round_i = cut_helper(prices, remaining - i, partial + prices[i])
            if round_i > best:
                best = round_i

        return best

    return cut_helper(prices, 6, 0)





import pytest


@pytest.mark.parametrize("prices,expected", [
    ([0, 1, 3, 3, 8, 8, 10], 11)
])
def test_rod_cutting(prices, expected):
    # assert(rod_cutting_recursive_6way2(prices) == expected)
    # assert(rod_cutting_recursive_6way2_memoize(prices) == expected)
    assert(rod_cutting_iterative_6way(prices) == expected)


pytest.main()
