def findMaxPossibleArea(heights, l, r):
    hl = len(heights)
    if l > r or l >= hl or r >= hl:
        return 0
    elif l == r:
        heights[l]

    mx = 0
    prev_h = heights[l]
    tracker = [[prev_h, 1]]
    for i in range(l + 1, r + 1):
        h = heights[i]
        if h >= prev_h:
            for item in tracker:
                item[1] += 1

            if h > prev_h:
                tracker.append([h, 1])

        else:
            j = 0
            cutoff = -1
            carryover = 0
            for item in tracker:
                if item[0] > h:
                    if cutoff < 0:
                        cutoff = j
                        carryover = item[1] + 1

                    mx = max(mx, item[0] * item[1])
                else:
                    item[1] += 1

                j += 1

            if cutoff >= 0:
                tracker = tracker[:cutoff]

                if cutoff == 0 or tracker[cutoff - 1] != h:
                    tracker.append([h, carryover])

        prev_h = h

    for item in tracker:
        mx = max(mx, item[0] * item[1])

    return mx

