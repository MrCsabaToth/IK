from collections import OrderedDict

def implement_LRU_cache(capacity, query_type, key, value):
    od = OrderedDict()
    ret = []

    length = len(query_type)
    i = 0
    while i < length:
        if query_type[i]:
            if len(od) < capacity or key[i] in od:
                od.pop(key[i], None)
            else:
                od.popitem(last=False)

            od[key[i]] = value[i]
        else:
            if key[i] in od:
                v = od.pop(key[i], None)
                ret.append(v)
                od[key[i]] = v
            else:
                ret.append(-1)

        i += 1

    return ret
