# Complete the 'nearest_neighbours' function below.
# The function accepts integer p_x, p_y, k and a 2D integer array n_points as parameter.

import heapq

class Pt(object):
    def __init__(self, x, y, p_x, p_y):
        self.x = x
        self.y = y
        self.ds = (p_x - x) * (p_x - x) + (p_y - y) * (p_y - y)

    def __lt__(self, other):
        return self.ds < other.ds

def nearest_neighbours(p_x, p_y, k, points):
    heap = [Pt(p[0], p[1], p_x, p_y) for p in points]
    heapq.heapify(heap)
    cluster = []
    for r in range(k):
        pt = heapq.heappop(heap)
        cluster.append([pt.x, pt.y])

    return cluster

