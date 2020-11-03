cache = {}

def is_prime(n):
    if n in cache:
        cache[n]

    if n < 2:
        return False
    elif n < 4:
        return True

    sq = int(n**.5 + 0.5)
    for i in range(2, sq + 1):
        if n % i == 0:
            cache[n] = False
            return False

    cache[n] = True
    return True

def detect_primes(a):
    ret = ""
    for n in a:
        ret += "1" if is_prime(n) else "0"

    return ret

