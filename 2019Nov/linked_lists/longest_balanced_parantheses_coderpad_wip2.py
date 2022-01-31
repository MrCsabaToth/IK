import queue

def find_max_length_of_matching_parentheses(brackets):
    # 1. Trim closing bracket prefixes
    i = 0
    while i < len(brackets) and brackets[i] == ')':
        i += 1

    longest = 0
    current = 0
    run = 0
    # 2. Now we roll
    q = queue.Queue()
    last = ''
    while i < len(brackets):
        print(i, brackets[i], run, current, longest)
        if brackets[i] == '(':
            q.put(1)
            if last == ')':
                current += run
                run = 0
        elif brackets[i] == ')':
            if not q.empty():
                q.get()
                run += 2
                if q.empty():
                    current += run
                    run = 0
            else:
                longest = max(longest, current)
                run = 0
                current = 0

        last = brackets[i]
        print(i, brackets[i], run, current, longest)
        i += 1

    longest = max(longest, current)

    return longest


import pytest


@pytest.mark.parametrize("s,expected", [
    ("((((())(((()", 4),
    ("(()", 2),
    ("(((()))", 6),
])
def test_find_max_length_of_matching_parentheses(s, expected):
    num = find_max_length_of_matching_parentheses(s)
    assert num == expected


pytest.main()

