def my_intersect(a, b):
    ap = 0
    bp = 0
    inter = []

    while ap < len(a) and bp < len(b):
        av = a[ap]
        bv = b[bp]
        if av < bv:
            while ap < len(a) and a[ap] == av:
                ap += 1
        elif av > bv:
            while bp < len(b) and b[bp] == bv:
                bp += 1
        else:  # av == bv
            inter.append(av)
            while ap < len(a) and a[ap] == av:
                ap += 1

            while bp < len(b) and b[bp] == bv:
                bp += 1

    return inter


import pytest
import random
import itertools


@pytest.mark.parametrize("i", range(50))
def test_intersect(i):
    rng = random.SystemRandom()
    al = [[rng.randint(1, 100)] * rng.randint(1, 3) for x in range(rng.randint(10, 20))]
    bl = [[rng.randint(1, 100)] * rng.randint(1, 3) for x in range(rng.randint(10, 20))]
    flatten = itertools.chain.from_iterable
    a = list(flatten(al))
    b = list(flatten(bl))
    a.sort()
    b.sort()
    result = my_intersect(a, b)
    a_set = set(a)
    b_set = set(b)
    expected = list(a_set.intersection(b_set))
    expected.sort()
    assert result == expected


pytest.main()
