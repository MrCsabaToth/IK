def merge_using_blank_space(arr1, arr2):
    a1 = len(arr1) - 1
    a2 = a1
    vacant = len(arr2) - 1

    while vacant >= 0:
        if a2 >= 0 and (a1 < 0 or arr2[a2] > arr1[a1]):
            arr2[vacant] = arr2[a2]
            a2 -= 1
        elif a1 >= 0:
            arr2[vacant] = arr1[a1]
            a1 -= 1

        vacant -= 1

    return arr2


import pytest
import random
import itertools


@pytest.mark.parametrize("i", range(50))
def test_merge_using_blank_space(i):
    flatten = itertools.chain.from_iterable
    rng = random.SystemRandom()
    n = rng.randint(20, 50)
    arr1 = [[rng.randint(1, 100)] * rng.randint(1, 3) for x in range(n)]
    arr1 = list(flatten(arr1))
    arr1.sort()

    n = len(arr1)
    arr2 = [[rng.randint(1, 100)] * rng.randint(1, 3) for x in range(2 * n)]
    arr2 = list(flatten(arr2))[:n]
    arr2.sort()
    arr_save = list(arr2)
    arr2.extend([None] * n)

    result = merge_using_blank_space(arr1, arr2)
    arr_save.extend(arr1)
    assert result == sorted(arr_save)


pytest.main()
