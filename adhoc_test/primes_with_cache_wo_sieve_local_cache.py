def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True

    sq = int(n**.5 + 0.5)
    for i in range(2, sq + 1):
        if n % i == 0:
            return False

    return True

def detect_primes(a):
    cache = {}
    ret = ""
    for n in a:
        if n in cache:
            part = cache[n]
        else:
            part = "1" if is_prime(n) else "0"
            cache[n] = part
        ret += part

    return ret

