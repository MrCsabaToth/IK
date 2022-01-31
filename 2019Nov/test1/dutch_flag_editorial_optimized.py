FIRST_CHAR = 'R'
SECOND_CHAR = 'G'
THIRD_CHAR = 'B'

ALPHABET = [FIRST_CHAR, SECOND_CHAR, THIRD_CHAR]


# RRRRRRGGGGGGGGGGBBBBBBBBB
def dutch_flag_sort(balls):
    length = len(balls)
    if length <= 1:
        return balls

    start = 0
    end = length - 1
    runner = 0
    while runner <= end:
        if balls[runner] == FIRST_CHAR:
            if balls[start] != FIRST_CHAR:
                balls[start], balls[runner] = balls[runner], balls[start]

            start += 1
            runner += 1
        elif balls[runner] == SECOND_CHAR:
            runner += 1
        else:  # balls[runner] == THIRD_CHAR:
            if balls[end] != THIRD_CHAR:
                balls[end], balls[runner] = balls[runner], balls[end]

            end -= 1

    return balls


import pytest
import random


@pytest.mark.parametrize("i", range(50))
def test_dutch_flag_sort(i):
    rng = random.SystemRandom()
    balls = []
    for alpha in ALPHABET:
        balls.extend([alpha] * rng.randint(0, 30))

    rng.shuffle(balls)
    print(balls)
    result = dutch_flag_sort(balls)
    print(result)
    assert result == sorted(balls, reverse=True)


pytest.main()
