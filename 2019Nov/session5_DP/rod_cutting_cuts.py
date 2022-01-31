# Fail to get it this way
def rod_cutting_recursive_6way2_memoize(prices):
    memo = dict()
    def cut_helper(remaining):
        if remaining == 0:
            return 0, []

        if remaining in memo:
            return memo[remaining]

        best = 0
        cuts = None
        for i in range(1, remaining + 1):
            price_i, cuts_i = cut_helper(remaining - i)
            round_i = prices[i] + price_i

            if round_i > best:
                best = round_i
                cuts = cuts_i

        cuts.append(i)
        memo[remaining] = (best, cuts)
        return best, cuts

    max_price, cuts = cut_helper(6)
    print(memo)
    return cuts


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

    # max_price = cache[n]
    # return max_price + 1

    cuts = []
    # partial = 0
    runner = n
    while runner > 1:
        for i in range(1, runner):
            if cache[runner] == cache[i] + prices[runner - i]:
                cuts.append(runner - i)
                runner = i
                break

    return cuts


def rod_cutting_iterative_6way_revcuts(prices):
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

    # max_price = cache[n]
    # return max_price + 1

    cuts = []
    # partial = 0
    runner = n
    while runner > 1:
        for i in range(1, runner):
            if cache[runner] == cache[runner - i] + prices[i]:
                cuts.append(i)
                runner -= i
                break

    return cuts


def rod_cutting_iterative_6way_fastcuts(prices):
    n = len(prices)
    cache = [(0, 0)] * (n + 1)
    for runner in range(1, n + 1):
        best = 0
        cut = None
        back = min(n, runner)
        for i in range(1, back):
            part, _ = cache[runner - i]
            partial = prices[i] + part
            if partial > best:
                best = partial
                cut = i

        cache[runner] = (best, cut)

    # max_price = cache[n][0]
    # return max_price + 1

    cuts = []
    # partial = 0
    runner = n
    while runner > 1:
        _, cut = cache[runner]
        cuts.append(cut)
        runner -= cut

    print(cache)
    return cuts


import pytest


@pytest.mark.parametrize("prices,expected,cuts", [
    ([0, 1, 3, 3, 8, 8, 10], 11, [4, 2])
])
def test_rod_cutting(prices, expected, cuts):
    assert(rod_cutting_iterative_6way(prices) == cuts)



@pytest.mark.parametrize("prices,expected,cuts", [
    ([0, 1, 3, 3, 8, 8, 10], 11, [2, 4])
])
def test_rod_cutting_rev(prices, expected, cuts):
    assert(rod_cutting_iterative_6way_revcuts(prices) == cuts)
    assert(rod_cutting_iterative_6way_fastcuts(prices) == cuts)


pytest.main()
