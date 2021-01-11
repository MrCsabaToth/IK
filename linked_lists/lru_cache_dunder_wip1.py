from collections import OrderedDict

class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        if key not in self:
            return -1

        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]


def implement_LRU_cache(capacity, query_type, key, value):
    od = LRU(capacity)
    ret = []

    length = len(query_type)
    i = 0
    while i < length:
        if query_type[i]:
            # if len(od) < capacity or key[i] in od:
            #     od.pop(key[i], None)
            # else:
            #     od.popitem(last=False)

            od[key[i]] = value[i]
        else:
            # if key[i] in od:
            #     v = od.pop(key[i], None)
            #     ret.append(v)
            #     od[key[i]] = v
            # else:
            #     ret.append(-1)
            ret.append(od[key[i]])

        i += 1

    return ret
