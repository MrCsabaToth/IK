def find_all_well_formed_brackets(n):
    result = []
    length = 2 * n
    slate = [None] * (2 * n)

    def bracket_helper(idx, opener, closer):
        if closer > opener or closer > n or opener > n:
            return

        if idx == length:
            result.append("".join(slate))
            return

        slate[idx] = "("
        bracket_helper(idx + 1, opener + 1, closer)

        slate[idx] = ")"
        bracket_helper(idx + 1, opener, closer + 1)

    bracket_helper(0, 0, 0)

    return result
