def divide(a, b):
    flip = False
    if a < 0 and b >= 0 or a >= 0 and b < 0:
        flip = True

    a = abs(a)
    b = abs(b)

    if b == 1:
        return a if not flip else -a

    # Assemble b number base digit values
    last_b = b
    last_m = 1
    bs = [last_b]
    ms = [last_m]
    while last_b <= a:
        last_b = last_b + last_b
        last_m = last_m + last_m
        bs.append(last_b)
        ms.append(last_m)

    q = 0
    acc = 0
    for i in range(len(bs))[::-1]:
        if bs[i] + acc <= a:
            acc += bs[i]
            q += ms[i]

    if flip:
        q = -q

    return q

