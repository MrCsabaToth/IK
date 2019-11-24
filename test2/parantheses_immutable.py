def find_all_well_formed_brackets(n):
    result = []

    def bracket_helper(partial, opener, closer):
        if opener == n and closer == n:
            result.append(partial)
            return

        if closer > opener or closer > n or opener > n:
            return

        bracket_helper(partial + "(", opener + 1, closer)
        bracket_helper(partial + ")", opener, closer + 1)

    bracket_helper("", 0, 0)

    return result
