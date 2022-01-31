# Test problem 8520
# To compute modulo multiplicate inverse
# Cannot use division? "sudo make me a sandwitch" Yo.
def binpow(a, b, m):
    a = a % m
    res = 1
    while b > 0:
        if b % 2 > 0:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2
    return res

def getProductArray(nums):
    modulo = 1000000007
    num_zeros = 0
    l = len(nums)
    result = [0] * l
    accu = 1
    for r in range(l):
        if nums[r] == 0:
            num_zeros += 1
        else:
            accu = (accu * nums[r]) % modulo
            if num_zeros == 0:
                result[r] = binpow(nums[r], modulo - 2, modulo)
        if num_zeros > 1:
            return [0] * l

    for r in range(l):
        if num_zeros > 0:
            if nums[r] != 0:
                result[r] = 0
            else:
                result[r] = accu
        else:
            result[r] = (result[r] * accu) % modulo

    return result
