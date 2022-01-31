arr = [2, 3, -4, -9, -1, -7, 1, -5, -6]

def next_p(arr, l, x):
    print("px0", x)
    while x <= l - 1 and arr[x] < 0:
        x += 1
        print("px1", x)

    print("px2", x)
    return x


def next_n(arr, l, x):
    print("nx0", x)
    while x <= l - 1 and arr[x] >= 0:
        x += 1
        print("nx1", x)

    print("nx2", x)
    return x

l = len(arr)
n = next_n(arr, l, 0)
p = next_p(arr, l, 0)

i = 0
print("a0", i, n, p, l, arr)
while i < l and n < l and p < l:
    pos = i % 2 == 0
    print("pos", i, pos, n, p)
    if pos:
        if arr[i] < 1:
            # if only a swap needed, we can swap
            if p == n + 1:
                arr[n], arr[p] = arr[p], arr[n]
                n, p = p, n
            else:
                arr.insert(i, arr[p])
                print("arrp0", arr)
                del arr[p + 1]
                print("arrp1", arr)
                n += 1

        p = next_p(arr, l, p + 1)
    else:
        if arr[i] >= 0:
            # if only a swap needed, we can swap
            if n == p + 1:
                arr[n], arr[p] = arr[p], arr[n]
                n, p = p, n
            else:
                arr.insert(i, arr[n])
                print("arrn0", arr)
                del arr[n + 1]
                print("arrn1", arr)
                p += 1

        n = next_n(arr, l, n + 1)

    i += 1
    print("a1", i, n, p, l, arr)

print("a2", arr)
