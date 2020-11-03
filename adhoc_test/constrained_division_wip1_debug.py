a = 9
b = 3

bs = [0] * 18
ms = [0] * 18
bs[0] = b
ms[0] = 1
for i in range(1, 18):
    bs[i] = bs[i - 1] + bs[i - 1]
    ms[i] = ms[i - 1] + ms[i - 1]
    if bs[i] > a:
        break

print(i, bs)
print(ms)

q = 0
acc = 0
for j in range(i + 1)[::-1]:
    print("i0", j, q, acc)
    if bs[j] + acc <= a:
        print("add")
        acc += bs[j]
        q += ms[j]
        print("i1", j, q, acc)

print(q)
