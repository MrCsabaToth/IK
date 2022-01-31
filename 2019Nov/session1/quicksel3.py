import random

def quickselect3(a, k):
    target = len(a) - k
    return qsel3(a, 0, len(a) - 1, target)


def qsel3(l, start, end, target):
    if start >= end:
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
        pivot_extension = smaller - 1
        while pivot_extension > 0 and l[pivot_extension] == l[smaller] and pivot_extension != target:
            pivot_extension -= 1

        return qsel3(l, start, pivot_extension, target)
    else:  # smaller < target
        pivot_extension = smaller + 1
        while pivot_extension < len(l) - 1 and l[pivot_extension] == l[smaller] and pivot_extension != target:
            pivot_extension += 1

        return qsel3(l, pivot_extension, end, target)


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

    result = quickselect3(l, k)
    
    l.sort()

    expected = l[n - k]
    assert result == expected


pytest.main()
