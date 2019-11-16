def two_sum_helper(l, start, end, s):
    if start >= end:
        return None

    if l[start] + l[end] == s:
        return [start, end]

    sol1 = two_sum_helper(l, start + 1, end, s)
    if sol1:
        return sol1
    sol2 = two_sum_helper(l, start, end - 1, s)
    if sol2:
        return sol2


def two_sum(l, s):
    l.sort()
    return two_sum_helper(l, 0, len(l) - 1, s)


import pytest
import random


@pytest.mark.parametrize("i", range(50))
def test_intersect(i):
    rng = random.SystemRandom()
    al = [rng.randint(1, 100) for x in range(rng.randint(10, 20))]
    s = rng.randint(1, 200)
    result = two_sum(al, s)
    print(al, s)
    if result is not None:
        print(result)
        assert al[result[0]] + al[result[1]] == s


pytest.main()
