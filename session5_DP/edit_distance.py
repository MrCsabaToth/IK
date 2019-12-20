def edit_distance(s1, s2):
    s1l = len(s1)
    s2l = len(s2)
    dp = [None] * (s1l + 1)
    for i in range(s1l + 1):
        dp[i] = [None] * (s2l + 1)

    for i in range(s1l + 1):
        dp[i][s2l] = s1l - i

    for j in range(s2l + 1):
        dp[s1l][j] = s2l - j

    # for i in range(s1l + 1):
    #     print(dp[i])

    for i in range(s1l - 1, -1, -1):
        for j in range(s2l - 1, -1, -1):
            dp[i][j] = (dp[i + 1][j + 1] if s1[i] == s2[j] else
                        1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1]))

    # for i in range(s1l + 1):
    #     print(dp[i])

    return dp[0][0]


import pytest


@pytest.mark.parametrize("s1,s2,expected", [
    ("car", "ball", 3),
    ("geek", "gesek", 1),
    ("cat", "cut", 1),
    ("catu", "ucut", 3),
    ("sunday", "saturday", 3),
    ("sundayo", "osaturday", 5),
])
def test_edit_distance(s1, s2, expected):
    assert(edit_distance(s1, s2) == expected)
    assert(edit_distance(s2, s1) == expected)


pytest.main()
