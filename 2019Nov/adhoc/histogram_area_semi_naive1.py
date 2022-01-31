def findMaxPossibleArea(heights, l, r):
    hl = len(heights)
    if l > r or l >= hl or r >= hl:
        return 0
    elif l == r:
        heights[l]

    mx = 0
    prev_h = heights[l]
    tracker = [1] * prev_h
    for i in range(l + 1, r + 1):
        h = heights[i]
        if h >= prev_h:
            for j in range(prev_h):
                tracker[j] += 1
            if len(tracker) < h:
                tracker = tracker + ([1] * (h - len(tracker)))
            if h > prev_h:
                for j in range(prev_h, h):
                    tracker[j] = 1
        else:
            for j in range(h):
                tracker[j] += 1
            for j in range(h, prev_h):
                mx = max(mx, (j + 1) * tracker[j])
                tracker[j] = 0
        prev_h = h

    for i in range(len(tracker)):
        mx = max(mx, (i + 1) * tracker[i])

    return mx

