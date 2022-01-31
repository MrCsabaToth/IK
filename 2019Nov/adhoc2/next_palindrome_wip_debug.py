n = 47

digits = []
while n:
    digits.insert(0, n % 10)
    n = n // 10
    print("d1", digits)

if not digits:
    digits = [0]

print("d2", digits)

# Search for the first differring digit from the half back to the start
l = len(digits)
half = (l - 1) // 2
i = half
incd = False
print("l", l, half, i, incd)
while i >= 0:
    if digits[i] == digits[l - 1 - i]:
        print("i0", i)
        i -= 1
    else:
        print("i3", i, l - 1 - i, digits[i], digits[l - 1 - i])
        if digits[i] < digits[l - 1 - i]:
            digits[i] += 1
            incd = True

        break

    print("i1", i, digits)

# We can mirror the rest of the beginning to the end
while i >= 0:
    digits[l - 1 - i] = digits[i]
    i -= 1
    print("i2", i, digits)

# Make sure the number will be bigger if there wasn't an increase so far
if not incd:
    i = half
    digits[i] += 1
    if i != l - 1 - i:
        digits[l - 1 - i] += 1

# Fix digits incremented from 9 to 10
i = half
while i >= 0:
    carry = 0
    if digits[i] >= 9:
        digits[i] = 0
        digits[l - 1 - i] = 0
        carry = 1
        j = i + 1
        while j < half and carry:
            digit = digits[j] + carry
            if digit > 9:
                digit -= 10
            else:
                carry = 0

            digits[j] = digit
            digits[l - 1 - j] = digit
            j += 1

    i -= 1

pal = 0
mult = 1
for digit in digits[::-1]:
    pal += mult * digit
    mult *= 10

print(pal)

