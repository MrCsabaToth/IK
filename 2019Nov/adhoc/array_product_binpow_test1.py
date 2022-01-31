ef binpow(a, b, m):
    a = a % m
    res = 1
    while b > 0:
        if b % 2 > 0:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2
    return res

import pytest
from hypothesis import given, strategies, example

@given(
    test_a=strategies.integers(min_value=1, max_value=500000000000000),
)
@example(test_a=760413902)
@example(test_a=602596170)
@example(test_a=203380689)
@example(test_a=523474641)
@example(test_a=264736937)
@example(test_a=267160837)
@example(test_a=425135053)
@example(test_a=224634588)
@example(test_a=625997852)
@example(test_a=615309822)
@example(test_a=490616828)
@example(test_a=343045843)
@example(test_a=191739512)
@example(test_a=411443454)
@example(test_a=752185093)
@example(test_a=869112221)
@example(test_a=263777925)
@example(test_a=218864734)
@example(test_a=176705299)
@example(test_a=947671206)
@example(test_a=698680924)
@example(test_a=766655647)
@example(test_a=106892731)
@example(test_a=341483289)
def test_binpow(test_a):
    modulo = 1000000007
    mod_inverse = binpow(test_a, modulo - 2, modulo)
    assert (test_a * mod_inverse) % modulo == 1

pytest.main()
