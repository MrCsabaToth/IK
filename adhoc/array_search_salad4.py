arr = [[1, 2, 3, 12],
  [4, 5, 6, 45],
  [7, 8, 9, 78]]
x = 12

print("start")

w = len(arr)
h = len(arr[0])
i = 0
j = 0
ibak = -1
jbak = -1
while i < w and j < h and arr[i][j] < x and (i != ibak or j != jbak):
  ibak = i
  jbak = j
  print("ij", i, j)
  ib = i
  ie = w - 1
  i2 = -1
  print("ibe", ib, ie)
  while ib < ie:
    i2n = ib + (ie - ib) // 2 + 1
    print("i2pre", i2n, i2, ib, ie)
    if i2 == i2n:
      print("bi")
      break
    i2 = i2n
    print("i2post", i2, ib, ie)
    if arr[i2][j] < x:
      ib = i2 + 1
    elif arr[i2][j] == x:
      print("present")
      break
    else:
      ie = max(0, i2 - 1)
    print("ibe2", ib, ie)

  while arr[i2][j] > x and i2 > i:
    print("i back")
    i2 -= 1
  if arr[i2][j] == x:
    print("present")
    break
  elif arr[i2][j] > x:
    print("not present")
  if i2 >= 0:
    i = i2
  print("i", i)

  jb = j
  je = h - 1
  j2 = -1
  print("jbe", jb, je)
  while jb < je:
    j2n = jb + (je - jb) // 2 + 1
    print("j2pre", j2n, j2, jb, je)
    if j2 == j2n:
      print("bj")
      break
    j2 = j2n
    print("j2post", j2, jb, je)
    if arr[i][j2] < x:
      jb = j2 + 1
    elif arr[i][j2] == x:
      print("present")
      break
    else:
      je = max(0, j2 - 1)
    print("jbe2", jb, je)

  while arr[i][j2] > x and j2 > j:
    print("j back")
    j2 -= 1
  if arr[i][j2] == x:
      print("present")
  elif arr[i][j2] > x:
      print("not present")
  if j2 >= 0:
    j = j2
  print("j", j2)

print("present" if arr[i][j] == x else "not present")

