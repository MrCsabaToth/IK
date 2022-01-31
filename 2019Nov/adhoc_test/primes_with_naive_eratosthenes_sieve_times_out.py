def detect_primes(a):
    l = 4000000
    flag = [True] * l
    flag[0] = False
    flag[1] = False
    for i in range(2, l):
        if flag[i]:
            x = i * 2
            while x < l:
                flag[x] = False
                x += i

    return "".join(["1" if flag[n] else "0" for n in a])

