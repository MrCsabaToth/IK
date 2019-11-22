def all_perm_helper(items, partial):
    if len(items) == 0:
        return ["".join(partial)]

    accumulator = []
    for item in items:
        partial.append(item)
        items.remove(item)

        result = all_perm_helper(items, partial)
        accumulator.extend(result)

        items.append(item)
        partial.remove(item)

    return accumulator


def all_perm(items):
    return all_perm_helper(items, [])
