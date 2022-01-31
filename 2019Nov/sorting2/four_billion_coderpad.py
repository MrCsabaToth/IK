def find_integer(arr):
    bits = 4
    diff = 64
    # We assume 64 bit integers
    # import sys
    # print(sys.maxsize)
    aux = [0] * (2 ** bits)
    filled = 2 ** diff - 1
    print(filled)
    for a in arr:
        i = a // diff
        r = a % diff
        flag = 1 << r
        aux[i] |= flag
        print(aux)

    i = 0
    base = 0
    for a in aux:
        if a < filled:
            k = 0
            while a > 0:
                if a % 2 == 0:
                    return base + k

                a //= 2
                k += 1

            return base + k

        base += diff
        i += 1

    return -1


import pytest


def test_find_integer():
    a = [0, 1, 2, 3]
    num = find_integer(a)
    assert num == 4


pytest.main()
