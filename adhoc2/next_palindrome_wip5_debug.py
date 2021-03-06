# 258 (262) 495 (505) 2993 (3003)
# 7558 (7667) 59999997 (60000006)
# 599999997 (600000006)
# 914273419 (914282419) 814373419 (814383418)
n = 814373419

# Dissect number into digits
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
            incd = True
            j = i + 1
            carry = 1
            while j <= half:
                digit = digits[j] + carry
                digits[j] = digit % 10
                digits[l - 1 - j] = digit % 10
                carry = digit // 10
                j += 1

            if carry:
              digits[i] += 1

        break

    print("i1", i, digits)

# We can mirror the rest of the beginning to the end
while i >= 0:
    if digits[l - 1 - i] < digits[i]:
      incd = True
    digits[l - 1 - i] = digits[i]
    i -= 1
    print("i2", i, digits)

# Make sure the number will be bigger if there wasn't an increase so far
if not incd:
    i = half
    digits[i] += 1
    print("corr", i, digits)
    if i != l - 1 - i:
        digits[l - 1 - i] += 1
        print("corr", i, digits)

# Fix digits incremented from 9 to 10
i = half
carry = 0
while i >= 0:
    digit = digits[i] + carry
    print("fix0", i, carry, digits[i], digit, digits)
    if carry or digit >= 9:
        digits[i] = digit % 10
        digits[l - 1 - i] = digit % 10

        carry = digit // 10

    print("fix1", i, carry, digits[i], digits)
    i -= 1

# Final touch for the fix
if carry:
  digits[0] = 1
  digits.append(1)

# Assemble number back from digits
pal = 0
mult = 1
for digit in digits:
    pal += mult * digit
    mult *= 10

print(pal)

