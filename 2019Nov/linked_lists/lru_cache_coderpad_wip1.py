from collections import OrderedDict

def implement_LRU_cache(capacity, query_type, key, value):
    od = OrderedDict()
    ret = []

    length = len(query_type)
    i = 0
    while i < length:
        if query_type[i]:
            if len(od) < capacity:
                od.pop(key[i], None)
            else:
                od.popitem(last=True)

            od[key[i]] = value[i]
        else:
            ret.append(od[key[i]] if key[i] in od else -1)

        print(i, od)
        i += 1

    print(ret)
    return ret


import pytest


@pytest.mark.parametrize("capacity,query_type,key,value,expected", [
    (3,
    [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [5, 4, 1, 2, 2, 2, 3, 2, 5, 4, 4, 2, 4, 3, 5],
    [5, 3, 4, 4, 1, 4, 5, 1, 2, 3, 3, 3, 3, 1, 3],
    [-1, 1, 1, -1, 1, 3, -1]),
])
def test_ordered_dict(capacity,query_type,key,value,expected):
    ret = implement_LRU_cache(capacity, query_type, key, value)
    length = len(ret)
    assert length == len(expected)
    i = 0
    while i < length:
        assert ret[i] == expected[i]
        i += 1


pytest.main()
