buildings = [[2, 9, 10],
[3, 7, 15],
[5, 12, 12],
[15, 20, 10],
[19, 24, 8],
]

# 1. Processing
bldg = buildings[0]
horizon = [0] * bldg[0] + [bldg[2]] * (bldg[1] - bldg[0])
print(horizon)
for bldg in buildings[1:]:
    print(bldg)
    l = len(horizon)
    if bldg[0] > l:
        horizon += [0] * (bldg[0] - l)
        horizon += [bldg[2]] * (bldg[1] - bldg[0])
    else:
        if bldg[1] > l:
            horizon += [bldg[2]] * (bldg[1] - l)

        for i in range(bldg[0], min(l, bldg[1])):
            horizon[i] = max(horizon[i], bldg[2])

    print(horizon)

# 2. Compiling output
out = []
lastH = horizon[0]
if lastH > 0:
    out.append([0, horizon[0]])

i = 1
for h in horizon[1:]:
    if h != lastH:
        out.append([i, h])

    i += 1
    lastH = h

out.append([i, 0])

print(out)

