import random

def quick_sort_helper(a, beg, end):
    length = end - beg + 1
    if length <= 1:
        return

    if length == 2:
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
    
    quick_sort_helper(a, beg, smaller - 1)
    quick_sort_helper(a, smaller + 1, end)


def quick_sort(a):
    quick_sort_helper(a, 0, len(a) - 1)


import pytest

@pytest.mark.parametrize("i", range(20))
def test_quick_sort(i):
    length = random.randint(10, 30)
    a = [random.randint(0, 1000) for j in range(length)]
    a2 = sorted(a)
    quick_sort(a)
    print(a)
    print(a2)
    for j in range(length):
        assert a[j] == a2[j]


@pytest.mark.parametrize("i", range(20))
def test_quick_sort_rng(i):
    rng = random.SystemRandom()
    length = rng.randint(10, 30)
    a = [rng.randint(0, 1000) for j in range(length)]
    a2 = sorted(a)
    quick_sort(a)
    print(a)
    print(a2)
    for j in range(length):
        assert a[j] == a2[j]


pytest.main()
