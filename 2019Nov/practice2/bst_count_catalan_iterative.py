def how_many_BSTs(n):
    if n < 3:
        return n

    ret = 1
    for k in range(2, n + 1):
        ret *= (n + k) / k

    return int(round(ret))
