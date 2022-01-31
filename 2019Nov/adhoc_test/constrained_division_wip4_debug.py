a = 1000000000000000000
b = 2

last_b = b
last_m = 1
bs = [last_b]
ms = [last_m]
while last_b <= a:
    last_b = last_b + last_b
    last_m = last_m + last_m
    bs.append(last_b)
    ms.append(last_m)

print(bs)
print(ms)

q = 0
acc = 0
for i in range(len(bs))[::-1]:
    print("i0", i, q, acc)
    if bs[i] + acc <= a:
        print("add")
        acc += bs[i]
        q += ms[i]
        print("i1", i, q, acc)

print(q)

