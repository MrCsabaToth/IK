arr = [[1, 2, 3, 12],
  [4, 5, 6, 45],
  [7, 8, 9, 78]]
x = 45

print("start")

w = len(arr)
h = len(arr[0])
print("wh", w, h)
i = 0
j = 0
while i < w and j < h:
  print("i", i, j)
  j = 0
  while j < h and arr[i][j] <= x:
    print("ij", i, j, arr[i][j])
    if arr[i][j] == x:
      print("present")
    j += 1
  # print("ij2", i, j, h, arr[i][j])
  # if arr[i][j] == x:
  #   print("present")
  if j >= h:
    j = 0
  i += 1
  print("ij3", i, j)

print("present" if i < w and j < h and arr[i][j] == x else "not present")

