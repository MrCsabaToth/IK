OPS = ["", "*", "+"]

def expr_helper(partial, index, target):
    # print(partial, index)
    if index > len(partial) - 1:
        print("leaf")
        if eval(partial) == target:
            print("found " + partial)
            return [partial]

        return []

    print("part " + partial[:index])
    if eval(partial[:index]) > target:
        return []

    result = []
    for op in OPS:
        # print("op {}".format(op))
        result.extend(expr_helper(partial[:index] + op + partial[index:], index + (2 if op else 1), target))

    return result


def generate_all_expressions(s, target):
    return expr_helper(s, 1, int(target))


import pytest


def test_expr_case():
    assert generate_all_expressions("050505", 5) == ""


pytest.main()
