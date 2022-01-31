def binpow(a, b, m):
    a = a % m
    res = 1
    while b > 0:
        if b % 2 > 0:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2
    return res

import pytest

@pytest.mark.parametrize("test_a", [
    760413902,
    602596170,
    203380689,
    523474641,
    264736937,
    267160837,
    425135053,
    224634588,
    625997852,
    615309822,
    490616828,
    343045843,
    191739512,
    411443454,
    752185093,
    869112221,
    263777925,
    218864734,
    176705299,
    947671206,
    698680924,
    766655647,
    106892731,
    341483289,
])
def test_binpow(test_a):
    modulo = 1000000007
    mod_inverse = binpow(test_a, modulo - 2, modulo)
    assert (test_a * mod_inverse) % modulo == 1

pytest.main()
