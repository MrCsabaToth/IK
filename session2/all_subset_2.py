def subset_helper(items, index, slate, inclusion):
    # Leaf node
    if index >= len(items):
        return ["".join(slate)]

    item = items[index]
    # Internal node
    # Exlude
    if items[index] not in inclusion or inclusion[item] <= 0:
        result = subset_helper(items, index + 1, slate, inclusion)
    else:
        result = []

    # Include
    if item in inclusion:
        inclusion[item] += 1
    else:
        inclusion[item] = 1

    slate.append(item)
    result.extend(subset_helper(items, index + 1, slate, inclusion))
    slate.pop()
    inclusion[item] -= 1

    return result


def subsets(items):
    slate = []
    inclusion = dict()
    return subset_helper(items, 0, slate, inclusion)
