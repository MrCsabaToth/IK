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
            if self.arr[mid] == val:
                i = mid
                while i >= 0 and self.arr[i] == val:
                    i -= 1

                return i + 1

            elif self.arr[mid] < val:
                low = mid + 1
            else:
                high = mid - 1

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
        self.arr.insert(pos, val)

    def log_remove(self, val):
        pos = self.log_search(val, True)
        if pos >= 0:
            self.arr.pop(pos)


def min_stack(operations):
    ret = []
    ll = SortedArray()
    q = []
    for op in operations:
        if op > 0:
            ll.log_insert(op)
            q.append(op)
        elif op == 0:
            ret.append(ll.arr[0] if q else -1)
        elif op < 0 and q:
            val = q.pop()
            ll.log_remove(val)

    return ret
