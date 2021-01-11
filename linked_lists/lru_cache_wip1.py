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

        i += 1

    return ret
