def parantheses_helper(opener, closer, n, slate):
    # Backtracking
    # if closer < opener:
    #     return []

    # Leaf node
    if opener == 0 and closer == 0:
        return ["".join(slate)]

    result = []
    # Internal node
    # Opener
    if opener > 0:
        slate.append("(")
        result.extend(parantheses_helper(opener - 1, closer, n, slate))
        slate.pop()

    # Closer
    if closer > opener and opener < n:
        slate.append(")")
        result.extend(parantheses_helper(opener, closer - 1, n, slate))
        slate.pop()

    return result


def parantheses(n):
    return parantheses_helper(n, n, n, [])
