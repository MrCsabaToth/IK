import operator, functools

def hammingWeight(n):
    w = 0
    while n > 0:
        w += n % 2
        n = n // 2
    return w

def calculateHammingWeight(s):
    return functools.reduce(lambda x,y: hammingWeight(y) + x, s, 0)

