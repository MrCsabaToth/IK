OPS = ["+", "*", ""]


def expr_helper(s, index, partial, target):
    partial_str = "".join(partial)
    # print(partial_str, index)
    if index >= len(s):
        partial2 = [(p if (len(p) == 1 or len(p) > 1 and p[0] != "0") else str(int(p))) for p in partial]
        partial_value = eval("".join(partial2))
        if partial_value == target:
            # print("found " + partial_str)
            return [partial_str]
        else:
            # print("nope {}".format(partial_value))
            return []

    result = []
    for op in OPS:
        char = s[index]
        if op == "":
            partial[-1] += char
        else:
            partial.extend([op, char])

        # print("rec " + "".join(partial), "op " + op)
        result.extend(expr_helper(s, index + 1, partial, target))

        if op == "":
            partial[-1] = partial[-1][:-1]
        else:
            partial.pop()
            partial.pop()

    return result


def generate_all_expressions(s, target):
    return expr_helper(s, 1, [s[0]], target)


import pytest


def test_expr_case():
    # 050505 5 60
    # 40404040 4 311
    assert len(generate_all_expressions("050505", 5)) == 60


pytest.main()
