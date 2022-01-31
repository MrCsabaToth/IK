arr = [[1, 2, 3, 12],
  [4, 5, 6, 45],
  [7, 8, 9, 78]]
x = 3

print("start")

w = len(arr)
h = len(arr[0])
i = 0
j = 0
while i < w and j < h and arr[i][j] < x:
  ib = i
  ie = w - 1
  i2 = -1
  while ib < ie:
    i2n = (ie - ib) // 2
    if i2 == i2n:
      break
    i2 = i2n
    print("i2 ", i2, ib, ie)
    if arr[i2][j] < x:
      ib = i2
    elif arr[i2][j] == x:
      print("present")
      break
    else:
      ie = i2

  while arr[i2][j] > x and i2 >= i:
    print("i back")
    i2 -= 1
  if arr[i2][j] == x:
    print("present")
    break
  elif arr[i2][j] > x:
    print("not present")
  i = i2
  print("i ", i)

  jb = j
  je = h - 1
  j2 = -1
  while jb < je:
    j2n = (je - jb) // 2
    print("j2n ", j2n)
    if j2 == j2n:
      print("b")
      break
    j2 = j2n
    print("j2 ", j2, jb, je)
    if arr[i][j2] < x:
      jb = j2
    elif arr[i][j2] == x:
      print("present")
      break
    else:
      je = j2

  while arr[i][j2] > x and j2 >= j:
    print("j back")
    j2 -= 1
  if arr[i][j2] == x:
      print("present")
  elif arr[i][j2] > x:
      print("not present")
  j = j2
  print("j ", j2)

print("present" if arr[i][j] == x else "not present")

