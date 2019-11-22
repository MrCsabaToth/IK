def case_perm_helper(slist, index):
    if index >= len(slist):
        return ["".join(slist)]

    char = slist[index]
    if not char.isalpha():
        return case_perm_helper(slist, index + 1)

    slist[index] = char.lower()
    result = case_perm_helper(slist, index + 1)
    slist[index] = char.upper()
    result.extend(case_perm_helper(slist, index + 1))
    return result


def case_permutations(string):
    return case_perm_helper([s for s in string], 0)
