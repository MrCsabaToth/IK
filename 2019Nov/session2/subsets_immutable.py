def subset_helper(items, index, slate):
    # Leaf node
    if index >= len(items):
        return ["".join(slate)]

    # Internal node
    # Exlude
    result = subset_helper(items, index + 1, slate)
    # Include
    slate.append(items[index])
    result.extend(subset_helper(items, index + 1, slate))
    slate.pop()
    return result


def subsets(items):
    slate = []
    return subset_helper(items, 0, slate)
