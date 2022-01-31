# arr = [2, 3, -4, -9, -1, -7, 1, -5, -6]
arr = [0, 0, 0, 0]

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
res = []

i = 0
print("a0", i, n, p, l, arr)
while i < l and n < l and p < l:
    pos = i % 2 == 0
    print("pos", i, pos, n, p)
    
    if pos:
      res.append(arr[p])
      p += 1
      p = next_p(arr, l, p)
    else:
      res.append(arr[n])
      n += 1
      n = next_n(arr, l, n)

    i += 1
    print("a1", i, n, p, l, res)

while i < l and n < l:
  if arr[n] < 0:
    res.append(arr[n])
  n += 1

while i < l and p < l:
  if arr[p] >= 0:
    res.append(arr[p])
  p += 1

print("a2", res)
