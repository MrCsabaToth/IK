# arr = [0, -1000, -100000, -10000000, -1000000000, 1000000000, 10000000, 100000, 1000, 10]
arr = [
  100,
64,
32,
4,
100000000,
100000,
1024,
512,
256,
]

asc = True
if (arr[0] > arr[1] and arr[1] > arr[2] or
    arr[0] < arr[1] and arr[1] > arr[2] and arr[0] < arr[2]):
    asc = False
print(asc)
b = 0
max_i = len(arr) - 1
e = max_i
while b < e:
    m = b + (e - b) // 2
    print(b, e, m)
    if arr[m] < arr[e] and asc or arr[m] > arr[e] and not asc:
        e1 = m
        e2 = max(m - 1, 0)
        print(e1, e2)
        if arr[e1] < arr[e2]: # and asc or arr[e1] > arr[e2] and not asc:
            print("e1")
            e = e1
        else:
            print("e2")
            e = e2
    else:
        b1 = m
        b2 = min(m + 1, max_i)
        print(b1, b2)
        if arr[b1] < arr[b2]: # and asc or arr[b1] > arr[b2] and not asc:
            print("b1")
            b = b1
        else:
            print("b2")
            b = b2
print(b, e, m, arr[b], arr[e], arr[m])

