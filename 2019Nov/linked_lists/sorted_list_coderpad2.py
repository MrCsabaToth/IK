class SortedArray:
    arr = None

    def __init__(self):
        self.arr = []

    def log_search(self, val, find):
        if not self.arr:
            return -1 if find else 0

        if not find and val > self.arr[-1]:
            return len(self.arr)

        low = 0
        high = len(self.arr) - 1
        while low <= high:
            mid = (low + high) // 2
            print(low, mid, high, self.arr)
            if self.arr[mid] == val:
                i = mid
                while i >= 0 and self.arr[i] == val:
                    i -= 1

                return i + 1

            elif self.arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

            print(self.arr, low, mid, high)

        if find:
            return -1

        low_val = self.arr[low]
        if low_val >= val and (low == 0 or self.arr[low - 1] <= val):
            return low

        high_val = self.arr[high]
        if high_val >= val and (high == 0 or self.arr[high - 1] <= val):
            return high

        return min(low, high)

    def log_insert(self, val):
        pos = self.log_search(val, False)
        print(val, pos, self.arr)
        self.arr.insert(pos, val)

    def log_remove(self, val):
        pos = self.log_search(val, True)
        if pos >= 0:
            self.arr.pop(pos)


import random
import pytest


@pytest.mark.parametrize("arr,val,expected", [
    ([12, 12, 25], 16, [12, 12, 16, 25])
])
def test_sorted_array_insert0(arr, val, expected):
    ll = SortedArray()
    ll.arr = arr[:]
    ll.log_insert(val)
    print(arr, ll.arr, expected)
    for i in range(len(expected)):
        assert ll.arr[i] == expected[i]


@pytest.mark.parametrize("i", range(100))
def test_sorted_array_insert(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 10)
    arr = [rng.randint(0, 100) for j in range(length)]
    sarr = sorted(arr)
    ll = SortedArray()
    [ll.log_insert(a) for a in arr]
    assert len(sarr) == len(ll.arr)
    print(arr, ll.arr, sarr)
    for i in range(len(sarr)):
        assert ll.arr[i] == sarr[i]


@pytest.mark.parametrize("i", range(100))
def test_sorted_array_remove(i):
    rng = random.SystemRandom()
    length = rng.randint(5, 10)
    arr = [rng.randint(0, 100) for j in range(length)]
    sarr = sorted(arr)
    ll = SortedArray()
    ll.arr = sarr[:]
    index = rng.randint(0, length - 1)
    ll.log_remove(sarr[index])
    expected = sarr[:]
    expected.pop(index)
    assert len(expected) == len(ll.arr)
    # print(arr, ll.arr, sarr)
    for i in range(len(expected)):
        assert ll.arr[i] == expected[i]


pytest.main()
