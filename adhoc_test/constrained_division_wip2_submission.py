def divide(a, b):
    flip = False
    if a < 0 and b >= 0 or a >= 0 and b < 0:
        flip = True

    a = abs(a)
    b = abs(b)

    # Assemble b number base digit values
    bs = [0] * 18
    ms = [0] * 18
    bs[0] = b
    ms[0] = 1
    for i in range(1, 18):
        bs[i] = bs[i - 1] + bs[i - 1]
        ms[i] = ms[i - 1] + ms[i - 1]
        if bs[i] >= a:
            break

    q = 0
    acc = 0
    for j in range(i + 1)[::-1]:
        if bs[j] + acc <= a:
            acc += bs[j]
            q += ms[j]

    if flip:
        q = -q

    return q
