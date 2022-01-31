def parantheses_helper(opener, closer, n, slate):
    # Backtracking
    if opener > closer or opener < 0 or closer < 0:
        return []

    # Leaf node
    if opener == 0 and closer == 0:
        return ["".join(slate)]

    result = []
    # Internal node
    # Opener
    slate.append("(")
    result.extend(parantheses_helper(opener - 1, closer, n, slate))
    slate.pop()

    # Closer
    slate.append(")")
    result.extend(parantheses_helper(opener, closer - 1, n, slate))
    slate.pop()

    return result


def parantheses(n):
    return parantheses_helper(n, n, n, [])
