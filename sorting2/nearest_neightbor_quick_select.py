# Complete the 'nearest_neighbours' function below.
# The function accepts integer p_x, p_y, k and a 2D integer array n_points as parameter.

# Using ../own/recursive_lomuto_quick_select_k_set_coderpad.py
# All tests (000-019) pass except 017 times out

class Pt(object):
    def __init__(self, x, y, p_x, p_y):
        self.x = x
        self.y = y
        self.ds = (p_x - x) * (p_x - x) + (p_y - y) * (p_y - y)

    def __lt__(self, other):
        return self.ds < other.ds

def quick_select_helper(a, beg, end, k):
    if beg >= end:
        return

    if end == beg + 1:
        if a[beg].ds > a[end].ds:
            a[beg], a[end] = a[end], a[beg]
        return

    pivot_index = random.randint(beg, end)
    pivot = a[pivot_index].ds
    # 1 swap pivot with beginning
    if pivot_index != beg:
        a[beg], a[pivot_index] = a[pivot_index], a[beg]

    # 2 scan rest fo the array and partition
    smaller = beg
    for bigger in range(beg + 1, end + 1):
        if a[bigger].ds < pivot:
            smaller += 1
            a[smaller], a[bigger] = a[bigger], a[smaller]

    # 3 swap back pivot with beginning
    a[beg], a[smaller] = a[smaller], a[beg]

    if smaller == k:
        return

    if smaller > k:
        quick_select_helper(a, beg, smaller - 1, k)
    else:
        quick_select_helper(a, smaller + 1, end, k)


def nearest_neighbours(p_x, p_y, k, points):
    pts = [Pt(p[0], p[1], p_x, p_y) for p in points]

    quick_select_helper(pts, 0, len(pts) - 1, k - 1)

    return [[pts[r].x, pts[r].y] for r in range(k)]
