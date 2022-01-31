def my_intersect3(a, b, c):
    ap = 0
    bp = 0
    cp = 0
    inter = []

    while ap < len(a) and bp < len(b) and cp < len(c):
        av = a[ap]
        bv = b[bp]
        cv = c[cp]
        if av == bv and bv == cv:
            inter.append(av)
            while ap < len(a) and a[ap] == av:
                ap += 1

            while bp < len(b) and b[bp] == bv:
                bp += 1

            while cp < len(c) and c[cp] == cv:
                cp += 1
        elif av == bv:
            if cv < av:
                while cp < len(c) and c[cp] == cv:
                    cp += 1
            else:
                while ap < len(a) and a[ap] == av:
                    ap += 1

                while bp < len(b) and b[bp] == bv:
                    bp += 1
        elif bv == cv:
            if av < bv:
                while ap < len(a) and a[ap] == av:
                    ap += 1
            else:
                while bp < len(b) and b[bp] == bv:
                    bp += 1

                while cp < len(c) and c[cp] == cv:
                    cp += 1
        elif av < bv:
            if cv < av:
                while cp < len(c) and c[cp] == cv:
                    cp += 1
            else:
                while ap < len(a) and a[ap] == av:
                    ap += 1
        else:  # av > bv
            if cv < bv:
                while cp < len(c) and c[cp] == cv:
                    cp += 1
            else:
                while bp < len(b) and b[bp] == bv:
                    bp += 1

    return inter


import pytest
import random
import itertools


@pytest.mark.parametrize("i", range(50))
def test_intersect(i):
    rng = random.SystemRandom()
    al = [[rng.randint(1, 10)] * rng.randint(1, 3) for x in range(rng.randint(10, 20))]
    bl = [[rng.randint(1, 10)] * rng.randint(1, 3) for x in range(rng.randint(10, 20))]
    cl = [[rng.randint(1, 10)] * rng.randint(1, 3) for x in range(rng.randint(10, 20))]
    flatten = itertools.chain.from_iterable
    a = list(flatten(al))
    b = list(flatten(bl))
    c = list(flatten(cl))
    a.sort()
    b.sort()
    c.sort()
    result = my_intersect3(a, b, c)
    a_set = set(a)
    b_set = set(b)
    c_set = set(c)
    expected = list(a_set.intersection(b_set).intersection(c_set))
    expected.sort()
    assert result == expected


pytest.main()
