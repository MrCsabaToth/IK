def check_helper(s, r, l):
    i = 0
    for i in range(l):
        if s[(i + r) % l] != s[(l - i - 1 + r) % l]:
            return False

    return True


def check_if_rotated(s):
    l = len(s)
    for r in range(l):
        if check_helper(s, r, l):
            return 1

    return 0

