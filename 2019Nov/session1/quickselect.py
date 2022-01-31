import random

def quickselect(a, k):
    target = len(a) - k
    return qsel(a, 0, len(a) - 1, target)


def qsel(l, start, end, target):
    if start == end:
        return l[start]  # start == target

    #Pick a random element as pivot
    randindex = random.randint(start, end)
    (l[randindex], l[start]) = (l[start], l[randindex])
    pivot = l[start]
    smaller = start
    bigger = start
    for bigger in range(start + 1, end + 1):
        if l[bigger] <= pivot:
            smaller += 1
            (l[smaller], l[bigger]) = (l[bigger], l[smaller])

    #Place pivot in the right spot
    (l[start], l[smaller]) = (l[smaller], l[start])

    if smaller == target:
        return l[target]
    if smaller > target:
        return qsel(l, start, smaller - 1, target)
    else:  # smaller < target
        return qsel(l, smaller + 1, end, target)


import pytest
import itertools


@pytest.mark.parametrize("i", range(50))
def test_quickselect(i):
    rng = random.SystemRandom()
    n = rng.randint(10, 20)
    k = rng.randint(5, n)

    ll = [[rng.randint(1, 100)] * rng.randint(1, 3) for x in range(n)]
    flatten = itertools.chain.from_iterable
    l = list(flatten(ll))
    n = len(l)

    result = quickselect(l, k)
    
    l.sort()

    expected = l[n - k]
    assert result == expected


pytest.main()
