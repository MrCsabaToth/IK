# arr = [0, -1000, -100000, -10000000, -1000000000, 1000000000, 10000000, 100000, 1000, 10]
# arr = [100, 64, 32, 4, 100000000, 100000, 1024, 512, 256]
arr = [6, 5, 4, 3, 2]

n = len(arr)
max_i = n - 1
asc = arr[0] - arr[max_i] > 0
b = 0
e = max_i

if arr[0] - arr[max_i] < 0 and arr[0] - arr[1] < 0 and arr[n - 2] - arr[max_i] < 0:
    print("spec1", arr[0])
    arr[0]
elif arr[0] - arr[max_i] > 0 and arr[0] - arr[1] > 0 and arr[n - 2] - arr[max_i] > 0:
    print("spec2", arr[max_i])
    arr[max_i]

print(n, b, e, asc)
while b <= e:
    if arr[b] - arr[e] <= 0 and asc:
        print("f1", arr[b])
        break
    elif arr[b] - arr[e] >= 0 and not asc:
        print("f2", arr[e])
        break

    m = (b + e) // 2
    print(b, e, m)
    if asc:
        if arr[m] - arr[b] >= 0:
            # Minimum is in right subarray
            b = m + 1;
            print("ba", b)
        else:
            # Minimum is in left subarray 
            e = m
            print("ea", e)
    else:
        if arr[m] - arr[b] < 0:
            # Minimum is in right subarray
            b = m
            print("bd", b)
        else:
            # Minimum is in left subarray
            e = m
            print("ed", e)

print(arr[b], arr[e], arr[m])

