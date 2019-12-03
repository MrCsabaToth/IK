import heapq

def topK(arr, k):
    acc = []
    for item in arr:
        if -item not in acc:
            heapq.heappush(acc, -item)

    return [-heapq.heappop(acc) for _ in range(k) if acc]
