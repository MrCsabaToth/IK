def log_search(arr, val, find):
    if not arr:
        return -1 if find else 0

    if not find and val > arr[-1]:
        return len(arr)

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

    return min(low, high)


def max_in_sliding_window(arr, w):
    win = sorted(arr[:w])
    rlen = len(arr) - w + 1
    ret = [None] * rlen
    m = win[-1]
    ret[0] = m
    for i in range(rlen - 1):
        out = arr[i]
        pos1 = log_search(win, out, True)
        print(out, pos1, win)
        if pos1 >= 0:
            win = win[:pos1] + win[pos1 + 1:]

        inp = arr[w + i]
        pos2 = log_search(win, inp, False)
        print(inp, pos2, win)
        win = [inp] + win[pos2+1:]
        m = win[-1]
        ret[i + 1] = m
        print(win, ret)

    return ret


import random
import pytest


@pytest.mark.parametrize("arr,w,expected", [
    ([1, 3, -1, -3, 5, 3, 6, 7,], 3, [3, 3, 5, 5, 6, 7,]),
    ([-5, 5], 1, [-5, 5]),
    ([6, 0, -6], 2, [6, 0]),
    ([73, 70, 3, 63, 4, 35], 3, [73, 70, 63, 63]),
])
def test_log_search_random(arr, w, expected):
    assert max_in_sliding_window(arr, w) == expected


@pytest.mark.parametrize("i", range(100))
def test_log_search_position(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 10)
    arr = [rng.randint(0, 100) for j in range(length)]
    w = 3
    wlen = length - w + 1
    win0 = [max(arr[i:i+w]) for i in range(wlen)]
    print(arr, win0, w)
    win1 = max_in_sliding_window(arr, w)
    assert len(win0) == wlen
    assert len(win0) == len(win1)
    for i in range(len(win0)):
        assert win0[i] == win1[i]


@pytest.mark.parametrize("i", range(1))
def test_log_search_insert(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 10)
    arr = [rng.randint(0, 100) for j in range(length)]
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
    if pos >= 0:
        assert arr[pos] < val
    else:
        assert arr[0] > val
    if pos < length - 1:
        assert arr[pos + 1] > val

    arr.insert(pos + 1, val)
    arr2 = sorted(arr)
    for i in range(len(arr)):
        assert arr[i] == arr2[i]


pytest.main()
