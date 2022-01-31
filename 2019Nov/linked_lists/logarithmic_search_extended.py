def log_search(arr, val, find):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            i = mid
            while i >= 0 and arr[i] == val:
                i -= 1

            return i + 1
        elif arr[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    if find:
        return -1

    print(low, mid, high)
    return max(min(low, high), 0)


import pytest
import random


@pytest.mark.parametrize("i", range(200))
def test_log_search_random(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 20)
    arr = [rng.randint(0, 1000) for j in range(length)]
    expected = rng.randint(0, length - 1)
    arr.sort()
    val = arr[expected]
    while expected >= 0 and arr[expected] == val:
        expected -= 1

    expected += 1
    pos = log_search(arr, val, True)
    print(arr, val, expected, pos)
    assert pos == expected


@pytest.mark.parametrize("i", range(10))
def test_log_search_min(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 20)
    arr = [rng.randint(0, 1000) for j in range(length)]
    expected = 0
    arr.sort()
    arr[expected] -= 1
    val = arr[expected]
    pos = log_search(arr, val, True)
    assert pos == expected


@pytest.mark.parametrize("i", range(10))
def test_log_search_max(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 20)
    arr = [rng.randint(0, 1000) for j in range(length)]
    expected = length - 1
    arr.sort()
    arr[expected] += 1
    val = arr[expected]
    pos = log_search(arr, val, True)
    assert pos == expected


@pytest.mark.parametrize("i", range(100))
def test_log_search_random_missing(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 20)
    arr = [rng.randint(0, 1000) for j in range(length)]
    arr.sort()
    target = rng.randint(0, length - 1)
    val = arr[target] - 1
    target -= 1
    while target >= 0 and arr[target] == val:
        val -= 1
        while target >= 0 and arr[target] == val:
            target -= 1

        target += 1

    pos = log_search(arr, val, True)
    print(arr, val, target, pos)
    assert pos == -1


@pytest.mark.parametrize("i", range(3))
def test_log_search_small_missing(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 20)
    arr = [rng.randint(0, 1000) for j in range(length)]
    arr.sort()
    pos = log_search(arr, arr[0] - i - 1, True)
    assert pos == -1


@pytest.mark.parametrize("i", range(3))
def test_log_search_big_missing(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 20)
    arr = [rng.randint(0, 1000) for j in range(length)]
    arr.sort()
    pos = log_search(arr, arr[-1] + i + 1, True)
    assert pos == -1


@pytest.mark.parametrize("i", range(100))
def test_log_search_position(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 20)
    arr = [rng.randint(0, 1000) for j in range(length)]
    arr.sort()
    target = rng.randint(0, length - 1)
    val = arr[target] - 1
    target -= 1
    while target >= 0 and arr[target] == val:
        val -= 1
        while target >= 0 and arr[target] == val:
            target -= 1

        target += 1

    target = max(target, 0)

    pos = log_search(arr, val, False)
    print(arr, val, target, pos)
    if pos > 0:
        assert arr[pos] < val
    if pos < length - 1:
        assert arr[pos + 1] > val


pytest.main()
