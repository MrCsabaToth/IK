CHARS = ['R', 'G', 'B']

def dutch_flag_sort(balls):
    max_index = len(balls) - 1
    r = 0
    g = 0
    b = max_index
    while g <= b:
        if balls[g] == CHARS[0]:
            if balls[r] != CHARS[0]:
                balls[r], balls[g] = balls[g], balls[r]

            r += 1
            g += 1
        elif balls[g] == CHARS[1]:
            g += 1
        else:  # balls[g] == CHARS[2]
            if balls[b] != CHARS[2]:
                balls[g], balls[b] = balls[b], balls[g]

            b -= 1


import pytest
import random
import copy


@pytest.mark.parametrize("i", range(50))
def test_flag(i):
    rng = random.SystemRandom()
    balls = []
    for alpha in CHARS:
        balls.extend([alpha] * rng.randint(0, 30))

    rng.shuffle(balls)
    print(balls)
    dutch_flag_sort(balls)
    print(balls)
    expected = copy.copy(balls)
    assert balls == sorted(expected, reverse=True)


pytest.main()
