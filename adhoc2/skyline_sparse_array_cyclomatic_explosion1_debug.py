buildings = (
[[1, 5, 2],
[2, 7, 4],
[3, 6, 3],
[4, 8, 4]]
)

#[[2, 9, 10],
#[3, 7, 15],
#[5, 12, 12],
#[15, 20, 10],
#[19, 24, 8]]

#[[1, 3, 5],
#[2, 4, 8],
#[8, 9, 1]]

#[[1, 2, 3],
#[2, 3, 3],
#[3, 4, 3],
#[4, 5, 3]]

# 1. Processing
bldg = buildings[0]
horizon = [[bldg[0], bldg[2]], [bldg[1], 0]]
print(horizon)
prev_lvl = bldg[2]
for bldg in buildings[1:]:
    print(bldg)
    # 1. binary search the entry point
    b = 0
    e = len(horizon) - 1
    print("be", b, e)
    while b < e:
      m = (b + e) // 2
      print("mbe", m, b, e)
      if horizon[m][0] > bldg[0]:
        e = m - 1
      else:
        b = m + 1
      print("be2", m, b, e)

    mn = min(b, e)
    mx = max(b, e)
    nl = horizon[mn][0] > bldg[0]
    xl = horizon[mx][0] > bldg[0]
    i = mx if xl else mn
    print("i", mn, mx, nl, xl, i)

    print("hb1", horizon[i], bldg)
    if horizon[i][0] < bldg[0]:
      horizon.append([bldg[0], bldg[2]])
      horizon.append([bldg[1], 0])
      i += 2
    else:
      while i < len(horizon) and bldg[0] <= horizon[i][0]:
        print("hb2", horizon[i], bldg, prev_lvl)
        print("horizon[i][1], bldg[2]", horizon[i][1], bldg[2])
        if horizon[i][1] < bldg[2]:
          if horizon[i][1] == 0:
            double_insert = bldg[1] < horizon[i][0]
            lvl = horizon[i - 1][1] if double_insert else 0
            print("di", double_insert, lvl, i)
            if bldg[0] < horizon[i - 1][0]:
              horizon[i][0] = bldg[1]
              print("sub1", horizon)
            else:
              if prev_lvl < bldg[2]:
                horizon.insert(i, [bldg[0], bldg[2]])
                print("ins1", horizon)
                prev_lvl = bldg[2]
                i += 1
                if i == len(horizon) - 1 or horizon[i + 1][0] > bldg[1]:
                  if horizon[i][0] < bldg[1]:
                    horizon[i][0] = bldg[1]
                    print("sub4", horizon)
                  else:
                    i -= 1
              elif prev_lvl == bldg[2]:
                if i == len(horizon) - 1 or horizon[i + 1][0] > bldg[1]:
                  horizon[i][0] = bldg[1]
                  print("sub2", horizon)
                i += 1
              elif i == 0 or horizon[i - 1][1] < bldg[2]:
                horizon[i][1] = bldg[2]
                print("sub3", horizon)
                i += 1
                horizon.insert(i, [bldg[1], 0])
                print("ins2", horizon)
            i += 1
            if double_insert and bldg[1] > horizon[i - 1][0]:
              horizon.insert(i, [bldg[1], lvl])
              print("dins", horizon)
              prev_lvl = lvl
              i += 1
            else:
              prev_lvl = bldg[2]
            i += 1
          elif prev_lvl == bldg[2]: # remove
            print("prev_lvl == bldg[2]", prev_lvl, bldg[2])
            horizon = horizon[:i] + horizon[i+1:]
            print("aft", horizon)
          else:
            print("horizon[i][1] = bldg[2]")
            horizon[i][1] = bldg[2]
            print("aft", horizon)
            i += 1

          prev_lvl = bldg[2]
        elif horizon[i][1] > bldg[2]:
          prev_lvl = horizon[i][1]
          i+= 1
        else:
          if prev_lvl == bldg[2]: # remove
            horizon = horizon[:i] + horizon[i+1:]
          else:
            i += 1

        print("horizon, lvl", horizon, prev_lvl)

    print("while end", horizon)

print("fin", horizon)

