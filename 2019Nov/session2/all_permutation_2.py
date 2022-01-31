def all_perm_helper(items, index, slate):
    # Leaf node
    if index == len(items):
        return ["".join(slate)]

    accumulator = []
    # Internal node
    dupcheck = dict()
    for pick in range(index, len(items)):  # index to len(items) - 1
        if items[pick] in dupcheck:
            continue

        dupcheck[items[pick]] = True

        items[index], items[pick] = items[pick], items[index]
        slate.append(items[index])

        result = all_perm_helper(items, index + 1, slate)
        accumulator.extend(result)

        slate.pop()
        items[index], items[pick] = items[pick], items[index]

    return accumulator


def all_perm(items):
    return all_perm_helper(items, 0, [])
