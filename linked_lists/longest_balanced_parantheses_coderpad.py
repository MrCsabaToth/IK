def find_max_length_of_matching_parentheses(brackets):
    i = 0
    longest = 0
    stack = []
    valid_from = 0
    while i < len(brackets):
        print(i, brackets[i], longest)
        if brackets[i] == '(':
            stack.append(i)
        else:
            if not stack:
                valid_from = i + 1;
            else:
                # pop
                stack = stack[:-1]
                substring_start = valid_from - 1 if not stack else stack[-1];
                substring_length = i - substring_start;
                longest = max(substring_length, longest)

        print(i, brackets[i], longest)
        i += 1

    return longest


import pytest


@pytest.mark.parametrize("s,expected", [
    ("(()", 2),
    (")()", 2),
    ("))", 0),
    ("(((()))", 6),
    ("((((())(((()", 4),
])
def test_find_max_length_of_matching_parentheses(s, expected):
    num = find_max_length_of_matching_parentheses(s)
    assert num == expected


pytest.main()
