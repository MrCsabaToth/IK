def case_perm_helper(string, index, slate):
    if index >= len(string):
        return ["".join(slate)]

    char = string[index]
    if not char.isalpha():
        slate.append(char)
        result = case_perm_helper(string, index + 1, slate)
        slate.pop()
        return result

    slate.append(char.lower())
    result = case_perm_helper(string, index + 1, slate)
    slate.pop()
    slate.append(char.upper())
    result.extend(case_perm_helper(string, index + 1, slate))
    slate.pop()
    return result


def case_permutations(string):
    return case_perm_helper(string, 0, [""])
