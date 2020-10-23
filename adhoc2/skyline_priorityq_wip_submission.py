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


def findSkyline(buildings):
    arr = []
    # 1. Pre-Processing
    for bldg in buildings:
      arr.append(BuildingSide(bldg[0], True, bldg[2]))
      arr.append(BuildingSide(bldg[1], False, bldg[2]))

    heapq.heapify(arr)

    height_count_q = {0: 1}
    max_height = 0
    horizon = []
    while arr:
      #bldg_side = arr[0]
      bldg_side = heapq.heappop(arr)
      # starting index signifies start of a buiding, so check if highest.
      if bldg_side.start:
        curr_count = height_count_q[bldg_side.height] if bldg_side.height in height_count_q else 0
        height_count_q[bldg_side.height] = curr_count + 1
        # if tallest buiding detected then update the skyline.
        if bldg_side.height > max_height:
          max_height = bldg_side.height
          horizon.append([bldg_side.index, bldg_side.height])
      # end index signifies end of a buiding, so remove it from the heightCountQ,
      # and update skyline if highest.
      else:
        if height_count_q[bldg_side.height] == 1:
          del height_count_q[bldg_side.height]
        else:
          height_count_q[bldg_side.height] += 1

        # update skyline, if tallest buiding ends.
        if max_height == bldg_side.height:
          last_val = sorted(height_count_q.items())[-1]
          if max_height != last_val[0]:
            horizon.append([bldg_side.index, last_val[0]])

          height_count_q[last_val[0]] = last_val[1]
          max_height = last_val[0]

    return horizon


