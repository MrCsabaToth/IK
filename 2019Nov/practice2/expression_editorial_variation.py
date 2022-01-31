OPS = ["+", "*", ""]


def generate_all_expressions(s, target):
    result = []
    length = len(s)

    def expr_helper(partial, accumulator, idx, prev):
        if idx == length:
            if accumulator == target:
                result.append(partial)  # partial is complete

            return

        for pos in range(idx, length):
            num_str = s[idx:pos + 1]
            num = int(num_str)
            if idx == 0:
                expr_helper(partial + num_str, num, pos + 1, num)
            else:
                expr_helper(partial + "+" + num_str, accumulator + num, pos + 1, num)
                expr_helper(partial + "*" + num_str, (accumulator - prev) + prev * num, pos + 1, prev * num)

    expr_helper("", 0, 0, 0)
    return result


import pytest


def test_expr_case():
    # 050505 5 60
    # 40404040 4 311
    assert len(generate_all_expressions("050505", 5)) == 60


pytest.main()
