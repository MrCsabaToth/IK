def two_sum_helper(l, start, end, s):
    if start >= end:
        return None

    summ = l[start] + l[end]
    if summ == s:
        return [l[start], l[end]]

    if summ < s:
        return two_sum_helper(l, start + 1, end, s)

    # sum > s
    return two_sum_helper(l, start, end - 1, s)


def two_sum(l, s):
    l2 = sorted(l)
    llen = len(l) - 1
    result = two_sum_helper(l2, 0, llen, s)
    if not result:
        return result

    return [l.index(result[0]), llen - l[::-1].index(result[1])]


import pytest
import random
import itertools


@pytest.mark.parametrize("i", range(50))
def test_two_sum(i):
    rng = random.SystemRandom()
    al = [[rng.randint(1, 400)] * rng.randint(1, 4) for x in range(rng.randint(10, 50))]
    # al = [rng.randint(1, 100) for x in range(rng.randint(10, 20))]
    flatten = itertools.chain.from_iterable
    al = list(flatten(al))
    als = sorted(al)
    aln = len(al)
    s = rng.randint(als[0] + als[1], als[aln - 1] + als[aln - 2])
    result = two_sum(al, s)
    print(al, s)
    if result is not None:
        print(result)
        assert al[result[0]] + al[result[1]] == s



# def test_two_sum2():
#     al = [230,863,916,585,981,404,316,785,88,
#           12,70,435,384,778,887,755,740,337,86,
#           92,325,422,815,650,920,125,277,336,221,
#           847,168,23,677,61,400,136,874,363,394,
#           199,863,997,794,587,124,321,212,957,
#           764,173,314,422,927,783,930,282,306,
#           506,44,926,691,568,68,730,933,737,531,
#           180,414,751,28,546,60,371,493,370,527,
#           387,43,541,13,457,328,227,652,365,430,
#           803,59,858,538,427,583,368,375,173,
#           809,896,370,789]
#     s = 542
#     result = two_sum(al, s)
#     if result is not None:
#         assert al[result[0]] + al[result[1]] == s


pytest.main()
