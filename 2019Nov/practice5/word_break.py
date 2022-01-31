def wordBreakCount(dictionary, txt):
    txtl = len(txt)
    maxw = 0
    d = dict()
    lens = set()
    for word in dictionary:
        wlen = len(word)
        maxw = max(wlen, maxw)
        if wlen not in d:
            d[wlen] = []

        d[wlen].append(word)
        lens.add(wlen)

    print(txtl, d, lens, maxw)

    dp = [0] * (txtl + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, txtl + 1):
        count = 0
        for j in lens:
            if i - j - 1 >= 0:
                print(i, j, i - j, txt[i - j - 1:i - 1])
                if txt[i - j - 1:i - 1] in d[j]:
                    count += dp[i - j]
                    print("*", count)

        dp[i] = count

    print(dp)
    return dp[txtl]


import pytest


@pytest.mark.parametrize("dictionary,txt,expected", [
    ([
        "kick",
        "start",
        "kickstart",
        "is",
        "awe",
        "some",
        "awesome",
    ],
    "kickstartisawesome", 4),
])
def test_edit_distance(dictionary, txt, expected):
    assert(wordBreakCount(dictionary, txt) == expected)


pytest.main()
