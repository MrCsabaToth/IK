def find_max_length_of_matching_parentheses(brackets):
    right_count = 0
    left_count = 0
    longest = 0
    for br in brackets:
        if br == '(':
            left_count += 1
        else:
            right_count += 1

        if right_count > left_count:
            right_count = 0
            left_count = 0
        elif right_count == left_count:
            longest = max(longest, 2 * left_count)

    right_count = 0
    left_count = 0
    for br in brackets[::-1]:
        if br == '(':
            left_count += 1
        else:
            right_count += 1

        if right_count < left_count:
            right_count = 0
            left_count = 0
        elif right_count == left_count:
            longest = max(longest, 2 * left_count)

    return longest
