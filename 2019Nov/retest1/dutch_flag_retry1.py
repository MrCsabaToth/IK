def dutch_flag_sort(balls):
    max_index = len(balls) - 1
    r = 0
    g = 0
    b = max_index
    while g < b:
        while r <= max_index and balls[r] == 'R':
            r += 1

        if g < r:
            g = r

        while g <= max_index and balls[g] == 'G':
            g += 1

        while b >= 0 and balls[b] == 'B':
            b -= 1

        if r <= max_index:
            if balls[r] == 'G':
                if g <= max_index:
                    balls[r], balls[g] = balls[g], balls[r]
                    r += 1
                    g += 1

            else:  # balls[r] == 'B'
                if b >= 0:
                    balls[r], balls[b] = balls[b], balls[r]
                    r += 1
                    b -= 1

            if g < r:
                g = r


import pytest

@pytest.mark.parametrize("input,expected", [
    (['G', 'R'], ['R', 'G']),
    (['R', 'B'], ['R', 'B']),
    (['G', 'B'], ['G', 'B']),
])
def test_flag(input, expected):
    dutch_flag_sort(input)
    assert input == expected


pytest.main()
