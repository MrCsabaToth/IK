def findSkyline(buildings):
    # 1. Processing
    bldg = buildings[0]
    horizon = [0] * bldg[0] + [bldg[2]] * (bldg[1] - bldg[0])
    for bldg in buildings[1:]:
        l = len(horizon)
        if bldg[0] > l:
            horizon += [0] * (bldg[0] - l)
            horizon += [bldg[2]] * (bldg[1] - bldg[0])
        else:
            if bldg[1] > l:
                horizon += [bldg[2]] * (bldg[1] - l)

            for i in range(bldg[0], min(l, bldg[1])):
                horizon[i] = max(horizon[i], bldg[2])

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

    return out
