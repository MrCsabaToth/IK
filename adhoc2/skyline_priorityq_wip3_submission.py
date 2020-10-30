import heapq

class BuildingSide:
  index = -1
  start = True
  height = -1

  def __init__(self, index, start, height):
    self.index = index
    self.start = start
    self.height = height

  def __eq__(self, other):
    return (
      self.index == other.index and
      self.start == other.start and
      self.height == other.height
    )

  def __lt__(self, other):
    # A lower value of index gets priority
    if self.index != other.index:
      return self.index < other.index

    # If the index values are the same, starting entry gets priority.
    if self.start != other.start:
      return self.start

    # If two buildings are starting at the same index,
    # then BuildingIndex with higher height gets priority.
    if self.start:
      return self.height > other.height

    # If two buildings are ending at the same index,
    # then BuildingIndex with lower height gets priority.
    if self.end:
      return self.height < other.height


def get_bin_index(q, value):
  if not q:
    return 0

  b = 0
  e = len(q) - 1
  while b <= e:
    m = (b + e) // 2
    v = q[m][0]
    if v < value:
      b = m + 1
    elif v > value:
      e = m - 1
    else:
      return m

  if b < len(q) and q[b][0] == value:
    return b

  if e < len(q) and q[e][0] == value:
    return e

  return m


def ins_bin_point(q, idx, item):
  if idx >= len(q):
    q.append(item)
  else:
    if item[0] > q[idx][0]:
      idx += 1

    q.insert(idx, item)


def findSkyline(buildings):
    arr = []
    # 1. Pre-Processing
    for bldg in buildings:
      arr.append(BuildingSide(bldg[0], True, bldg[2]))
      arr.append(BuildingSide(bldg[1], False, bldg[2]))

    heapq.heapify(arr)

    height_count_q = [[0, 1]]
    max_height = 0
    horizon = []
    while arr:
      bldg_side = heapq.heappop(arr)
      # starting index signifies start of a buiding, so check if highest.
      if bldg_side.start:
        curr_i = get_bin_index(height_count_q, bldg_side.height)
        curr_count = height_count_q[curr_i][1] if height_count_q and height_count_q[curr_i][0] == bldg_side.height else 0
        if curr_count:
          height_count_q[curr_i][1] = curr_count + 1
        else:
          ins_bin_point(height_count_q, curr_i, [bldg_side.height, 1])
        # if tallest buiding detected then update the skyline.
        if bldg_side.height > max_height:
          max_height = bldg_side.height
          horizon.append([bldg_side.index, bldg_side.height])
      # end index signifies end of a buiding, so remove it from the heightCountQ,
      # and update skyline if highest.
      else:
        curr_i = get_bin_index(height_count_q, bldg_side.height)
        if height_count_q and height_count_q[curr_i][0] == bldg_side.height:
          if height_count_q[curr_i][1] == 1:
            del height_count_q[curr_i]
          else:
            height_count_q[curr_i][1] -= 1

        # update skyline, if tallest buiding ends.
        if max_height == bldg_side.height and height_count_q:
          last_val = height_count_q[-1]
          if max_height != last_val[0]:
            horizon.append([bldg_side.index, last_val[0]])

          height_count_q[-1][1] = last_val[1]
          max_height = last_val[0]

    return horizon

