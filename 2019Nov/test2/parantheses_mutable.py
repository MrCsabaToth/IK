def find_all_well_formed_brackets(n):
    result = []

    def bracket_helper(partial, opener, closer):
        if opener == n and closer == n:
            result.append("".join(partial))
            return

        if closer > opener or closer > n or opener > n:
            return

        partial.append("(")
        bracket_helper(partial, opener + 1, closer)
        partial.pop()

        partial.append(")")
        bracket_helper(partial, opener, closer + 1)
        partial.pop()

    bracket_helper([], 0, 0)

    return result
