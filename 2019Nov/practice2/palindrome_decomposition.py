def generate_palindromic_decompositions(s):
    result = []
    length = len(s)

    def is_palindrom(part):
        length = len(part)
        if length <= 1:
            return True

        start = 0
        end = len(part) - 1
        while start < end:
            if part[start] != part[end]:
                return False

            start += 1
            end -= 1

        return True

    def pal_help(partial, idx, pos):
        if idx == length:
            if all([is_palindrom(part) for part in partial.split("|")]):
                result.append(partial)

            return

        pal_help(partial, idx + 1, pos + 1)
        pal_help(partial[:pos] + "|" + partial[pos:], idx + 1, pos + 2)

    if length == 0:
        return []

    if length == 1:
        return [s]

    pal_help(s, 1, 1)

    return result
