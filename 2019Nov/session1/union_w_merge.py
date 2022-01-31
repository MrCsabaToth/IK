def my_union(a, b):
    ap = 0
    bp = 0
    union = []

    while ap < len(a) and bp < len(b):
        av = a[ap]
        bv = b[bp]
        if av < bv:
            union.append(av)
            while ap < len(a) and a[ap] == av:
                ap += 1
        elif av > bv:
            union.append(bv)
            while bp < len(b) and b[bp] == bv:
                bp += 1
        else:  # av == bv
            union.append(av)
            while ap < len(a) and a[ap] == av:
                ap += 1

            while bp < len(b) and b[bp] == bv:
                bp += 1

    while ap < len(a):
        av = a[ap]
        union.append(av)
        while ap < len(a) and a[ap] == av:
            ap += 1

    while bp < len(b):
        bv = b[bp]
        union.append(bv)
        while bp < len(b) and b[bp] == bv:
            bp += 1

    return union


import pytest
import random
import itertools


@pytest.mark.parametrize("i", range(50))
def test_union(i):
    rng = random.SystemRandom()
    al = [[rng.randint(1, 100)] * rng.randint(1, 3) for x in range(rng.randint(10, 20))]
    bl = [[rng.randint(1, 100)] * rng.randint(1, 3) for x in range(rng.randint(10, 20))]
    flatten = itertools.chain.from_iterable
    a = list(flatten(al))
    b = list(flatten(bl))
    a.sort()
    b.sort()
    result = my_union(a, b)
    a_set = set(a)
    b_set = set(b)
    expected = list(a_set.union(b_set))
    expected.sort()
    assert result == expected


pytest.main()
