import random

def quick_select_helper(a, beg, end, k):
    if beg >= end:
        return

    if end == beg + 1:
        if a[beg] > a[end]:
            a[beg], a[end] = a[end], a[beg]
        return

    pivot_index = random.randint(beg, end)
    pivot = a[pivot_index]
    # 1 swap pivot with beginning
    if pivot_index != beg:
        a[beg], a[pivot_index] = a[pivot_index], a[beg]

    # 2 scan rest fo the array and partition
    smaller = beg
    for bigger in range(beg + 1, end + 1):
        if a[bigger] < pivot:
            smaller += 1
            a[smaller], a[bigger] = a[bigger], a[smaller]

    # 3 swap back pivot with beginning
    a[beg], a[smaller] = a[smaller], a[beg]

    if smaller == k:
        return

    # One half of the problem is not relevant any more, we hone in on the interesting part
    if smaller > k:
        quick_select_helper(a, beg, smaller - 1, k)
    else:
        quick_select_helper(a, smaller + 1, end, k)


def quick_select(a, k):
    quick_select_helper(a, 0, len(a) - 1, k - 1)


import pytest


@pytest.mark.parametrize("i", range(30))
def test_quick_select_rng(i):
    rng = random.SystemRandom()
    length = rng.randint(10, 40)
    a = [rng.randint(0, 1000) for j in range(length)]
    k = length // 2
    a2 = sorted(a)
    print(length, k)
    quick_select(a, k)
    a3 = sorted(a2[:k])
    print(a)
    print(a2)
    print(a2[:k])
    print(a3)
    for j in range(k):
        assert a2[j] == a3[j]


pytest.main()
