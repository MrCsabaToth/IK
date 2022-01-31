def case_perm_helper(string, index, slate):
    if index >= len(string):
        return [slate]

    char = string[index]
    if not char.isalpha():
        return case_perm_helper(string, index + 1, slate + char)

    result = case_perm_helper(string, index + 1, slate + char.lower())
    result.extend(case_perm_helper(string, index + 1, slate + char.upper()))
    return result


def case_permutations(string):
    return case_perm_helper(string, 0, "")
