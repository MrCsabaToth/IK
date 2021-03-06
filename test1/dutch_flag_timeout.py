FIRST_CHAR = 'R'
SECOND_CHAR = 'G'
THIRD_CHAR = 'B'

ALPHABET = [FIRST_CHAR, SECOND_CHAR, THIRD_CHAR]


# RRRRRRGGGGGGGGGGBBBBBBBBB
def dutch_flag_sort(balls):
    start = 0
    end = len(balls) - 1
    mid = len(balls) // 2
    while start < end - 1:
        start_item = balls[start]
        end_item = balls[end]
        mid_item = balls[mid]
        if start_item == 'R':
            start += 1
        elif end_item == 'B':
            end -= 1
        elif start_item == 'G':
            if end_item == 'R':
                if mid_item == 'B':
                    balls[end], balls[mid] = balls[mid], balls[end]
                    end -= 1
                if mid_item == 'R':
                    balls[start], balls[end] = balls[end], balls[start]
                    start += 1
            else:  # end_item == 'G'
                if mid_item == 'R':
                    balls[start], balls[mid] = balls[mid], balls[start]
                    start += 1
                elif mid_item == 'B':
                    balls[end], balls[mid] = balls[mid], balls[end]
                    end -= 1
                else:  # mid_item == 'G'
                    mid = start + 1
        elif start_item == 'B':
            if end_item == 'R':
                balls[start], balls[end] = balls[end], balls[start]
                start += 1
                end -= 1
            else:  # end_item == 'G'
                if mid_item == 'R':
                    balls[start], balls[mid] = balls[mid], balls[start]
                    balls[end], balls[mid] = balls[mid], balls[end]
                    start += 1
                    end -= 1
                elif mid_item == 'B':
                    balls[start], balls[end] = balls[end], balls[start]
                    end -= 1
                else:  # mid_item == 'G'
                    balls[start], balls[end] = balls[end], balls[start]
                    end -= 1

        if mid == end:
            mid = start + 1
        # elif mid == start:
        #     mid = end - 1

    return balls


import pytest
import random


@pytest.mark.parametrize("i", range(1))
def test_dutch_flag_sort(i):
    rng = random.SystemRandom()
    balls = []
    for alpha in ALPHABET:
        balls.extend([alpha] * rng.randint(0, 5))

    rng.shuffle(balls)
    print(balls)
    result = dutch_flag_sort(balls)
    assert result == sorted(balls)[::-1]


pytest.main()
