arr = [2, 3, -4, -9, -1, -7, 1, -5, -6]

def find_next_pos(arr, l, x):
    print("px0", x)
    while arr[x] < 0 and x < l - 1:
        x += 1
        print("px1", x)

    print("px2", x)
    return x


def find_next_neg(arr, l, x):
    print("nx0", x)
    while arr[x] >= 0 and x < l - 1:
        x += 1
        print("nx1", x)

    print("nx2", x)
    return x


l = len(arr)
n = find_next_neg(arr, l, 0)
p = find_next_pos(arr, l, 0)

i = 0
print("a0", n, p, i, l, arr)
while i < l:
    pos = i % 2 == 0
    if pos:
        if arr[i] >= 0:
            p = find_next_pos(arr, l, i + 1)
        else:
            # if only a swap needed, we can swap
            if p == n + 1:
                arr[n], arr[p] = arr[p], arr[n]
                n, p = p, n
                p = find_next_pos(arr, l, p + 1)
            else:
                arr.insert(i, arr[p])
                del arr[p]
                n += 1
                p = find_next_pos(arr, l, p)
    else:
        if arr[i] < 0:
            p = find_next_pos(arr, l, i + 1)
        else:
            # if only a swap needed, we can swap
            if n == p + 1:
                arr[n], arr[p] = arr[p], arr[n]
                n, p = p, n
                n = find_next_pos(arr, l, n + 1)
            else:
                arr.insert(i, arr[n])
                del arr[n]
                p += 1
                n = find_next_pos(arr, l, n)

    i += 1
    print("a1", n, p, i, l, arr)

print("a2", arr)

