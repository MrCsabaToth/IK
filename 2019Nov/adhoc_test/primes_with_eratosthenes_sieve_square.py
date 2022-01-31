def is_prime(n, sieve, l):
    if n < l:
        return sieve[n]

    sq = int(n**.5 + 0.5)
    for i in range(2, min(sq + 1, l)):
        if sieve[i]:
            if n % i == 0:
                return False

    return True

def detect_primes(a):
    l = 2000
    sieve = [True] * l
    sieve[0] = False
    sieve[1] = False
    for i in range(2, l):
        if sieve[i]:
            x = i * 2
            while x < l:
                sieve[x] = False
                x += i

    return "".join(["1" if is_prime(n, sieve, l) else "0" for n in a])
