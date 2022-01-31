def min_stack(operations):
    ret = []
    q = []
    for op in operations:
        if op > 0:
            q.append(op if not q else min(op, q[-1]))
        elif op == 0:
            ret.append(q[-1] if q else -1)
        elif op < 0 and q:
            q.pop()

    return ret
