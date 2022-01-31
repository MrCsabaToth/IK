def find_max_length_of_matching_parentheses(brackets):
    # 1. Trim closing bracket prefixes
    i = 0
    while i < len(brackets) and brackets[i] == ')':
        i += 1

    longest = 0
    # 2. Now we roll
    stack = []
    valid_from = i
    while i < len(brackets):
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

        i += 1

    return longest
