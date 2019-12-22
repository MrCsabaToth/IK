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

    for i in range(s1l + 1):
        print(dp[i])

    return dp[0][0]



def levenshteinDistance(s1, s2):
    s1l = len(s1)
    s2l = len(s2)
    dp = [None] * (s1l + 1)
    for i in range(s1l + 1):
        dp[i] = [None] * (s2l + 1)

    # flipping the matrix horizontally and vertically
    # Why would we fill everything in reverse???
    for i in range(s1l + 1):
        dp[i][0] = i

    for j in range(s2l + 1):
        dp[0][j] = j


    for i in range(1, s1l + 1):
        for j in range(1, s2l + 1):
            dp[i][j] = (
                dp[i - 1][j - 1] if s1[i - 1] == s2[j - 1] else
                (1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]))
            )

    for i in range(s1l + 1):
        print(dp[i])

    return dp[s1l][s2l]



import pytest


@pytest.mark.parametrize("s1,s2,expected", [
    ("car", "ball", 3),
    ("geek", "gesek", 1),
    ("cat", "cut", 1),
    ("catu", "ucut", 3),
    ("sunday", "saturday", 3),
    ("sundayo", "osaturday", 5),
    ("cat", "bat", 1),
    ("pizza", "yolo", 5),
    ("kitten", "sitting", 3),  # 3
    ("a", "a", 0),
    ("e", "eqqqqqqqqq", 9),
    ("masilanidbny", "zwujtimkexcgvxrgkp", 17),
    ("fifsmivvlq", "fpypvzeidrssnwlxss", 15),
    ("dcygbpts", "hhebnnxixpm", 11),
    (
        "wvksnuxaldljqcjqnazsfoxqbylzhtcbvtpqqvkjhoqyrmdpjpxmzxvaulvbkyeyewlhuuutcpugkmqfhwwxwcdjyavnszhwth",
        "opszfjkvkzjbgltaqnzytzwhiupbrioyttquvttipgefsuawjwzmkmhomkjpnafyacssguytebhcltwmqivuekhzivcqxmqkgwrfihaviegiroozb",
        93
    ),
])
def test_edit_distance(s1, s2, expected):
    # assert(edit_distance(s1, s2) == expected)
    # assert(edit_distance(s2, s1) == expected)
    assert(levenshteinDistance(s1, s2) == expected)
    assert(levenshteinDistance(s2, s1) == expected)


pytest.main()
