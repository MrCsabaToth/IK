# Complete the function below.

def next_palindrome(n):
    digits = []
    while n:
        digits.insert(0, n % 10)
        n = n // 10

    if not digits:
        digits = [0]

    # Search for the first differring digit from the half back to the start
    l = len(digits)
    half = (l - 1) // 2
    i = half
    incd = False
    while i >= 0:
        if digits[i] == digits[l - 1 - i]:
            i -= 1
        else:
            if digits[i] < digits[l - 1 - i]:
                incd = True
                j = half
                carry = 1
                while j >= i and carry:
                    digit = digits[j] + carry
                    digits[j] = digit % 10
                    digits[l - 1 - j] = digit % 10
                    carry = digit // 10
                    j -= 1

                if carry:
                    digits[i] += 1

            break

    # We can mirror the rest of the beginning to the end
    while i >= 0:
        if digits[l - 1 - i] < digits[i]:
            incd = True
        digits[l - 1 - i] = digits[i]
        i -= 1

    # Make sure the number will be bigger if there wasn't an increase so far
    if not incd:
        i = half
        digits[i] += 1
        if i != l - 1 - i:
            digits[l - 1 - i] += 1

    # Fix digits incremented from 9 to 10
    i = half
    carry = 0
    while i >= 0:
        digit = digits[i] + carry
        if carry or digit >= 9:
            digits[i] = digit % 10
            digits[l - 1 - i] = digit % 10

            carry = digit // 10

        i -= 1

    if carry:
        digits[0] = 1
        digits.append(1)

    pal = 0
    mult = 1
    for digit in digits[::-1]:
        pal += mult * digit
        mult *= 10

    return pal
