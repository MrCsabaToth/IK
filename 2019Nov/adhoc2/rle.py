def RLE(strInput):
    out = ""
    if not strInput:
        return strInput

    lastCh = strInput[0]
    cnt = 1
    for ch in strInput[1:]:
        if ch != lastCh:
            if cnt == 1:
                out += lastCh
            else:
                out += f"{cnt}{lastCh}"
            lastCh = ch
            cnt = 1
        else:
            cnt += 1

    if cnt == 1:
        out += lastCh
    else:
        out += f"{cnt}{lastCh}"

    return out

