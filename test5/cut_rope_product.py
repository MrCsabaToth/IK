def max_product_from_cut_pieces(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        choices = [dp[i - j] * j for j in range(1, i // 2 + 1) if i - j >= 0]
        if i < n:
            choices.append(i)
        dp[i] = max(choices)

    print(dp)
    return dp[n]


import pytest


@pytest.mark.parametrize("n,expected", [
    (3, 2),
    (4, 4),
    (5, 6),
    (6, 9),
    (11, 54),
    (12, 81),
])
def test_max_product_from_cut_pieces(n, expected):
    assert(max_product_from_cut_pieces(n) == expected)


pytest.main()
