import random

def quicksort3(a):
    qsort3(a, 0, len(a) - 1)


def qsort3(l, start, end):
    if start >= end:
        return

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
    pivot_extension = smaller - 1
    while pivot_extension > 0 and l[pivot_extension] == l[smaller]:
        pivot_extension -= 1

    qsort3(l, start, pivot_extension)

    pivot_extension = smaller + 1
    while pivot_extension < len(l) - 1 and l[pivot_extension] == l[smaller]:
        pivot_extension += 1

    qsort3(l, pivot_extension, end)


import pytest
import itertools


@pytest.mark.parametrize("i", range(50))
def test_intersect(i):
    rng = random.SystemRandom()
    al = [[rng.randint(1, 100)] * rng.randint(1, 3) for x in range(rng.randint(10, 20))]
    flatten = itertools.chain.from_iterable
    a = list(flatten(al))
    quicksort3(a)
    assert a == sorted(a)


pytest.main()
