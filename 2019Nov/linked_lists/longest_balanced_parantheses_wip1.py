import queue

def find_max_length_of_matching_parentheses(brackets):
    # 1. Trim closing bracket prefixes
    i = 0
    while brackets[i] == ')':
        i += 1

    longest = 0
    current = 0
    # 2. Now we roll
    q = queue.Queue()
    while i < len(brackets):
        if brackets[i] == '(':
            q.put(1)
        elif brackets[i] == ')':
            if not q.empty():
                q.get()
                current += 2
            else:
                longest = max(longest, current)
                current = 0

        i += 1

    longest = max(longest, current)

    return longest
