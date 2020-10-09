heights = [6, 2, 5, 4, 5, 1, 6]
l = 0
r = 6

print("start")

hl = len(heights)
if l > r or l >= hl or r >= hl:
    print('yo')
elif l == r:
    heights[l]

leftSmaller = [None] * hl
stack = []
for i in range(l, r + 1):
  if not stack:
    leftSmaller[i] = i
  else:
    if heights[i] > heights[stack[-1]]:
      leftSmaller[i] = i
      stack.append(i)
    else:
      marker = 0
      while heights[stack[marker]] < heights[i]:
        leftSmaller[i] = stack[marker]
        marker += 1
      should_append = True
      if stack[marker] == heights[i]:
        marker += 1
        should_append = False
      stack = stack[:marker]
      if should_append:
        stack.append(i)

print(leftSmaller)

rightSmaller = [None] * hl
stack = []
for i in range(r, l, -1):
  if not stack:
    rightSmaller[i] = i
  else:
    if heights[i] > heights[stack[-1]]:
      rightSmaller[i] = i
      stack.append(i)
    else:
      marker = 0
      while heights[stack[marker]] < heights[i]:
        rightSmaller[i] = stack[marker]
        marker += 1
      should_append = True
      if stack[marker] == heights[i]:
        marker += 1
        should_append = False
      stack = stack[:marker]
      if should_append:
        stack.append(i)

print(rightSmaller)

mx = 0
for i in range(l + 1, r + 1):
    area = ((rightSmaller[i] - 1 - (leftSmaller[i] + 1)) + 1) * heights[i]
    print(area, rightSmaller[i], leftSmaller[i],  heights[i], mx)
    mx = max(mx, area)

print("finish", mx)

