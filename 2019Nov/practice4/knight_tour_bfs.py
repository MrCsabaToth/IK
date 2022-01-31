def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    # row_low = start_row if start_row < end_row else end_row
    # row_high = start_row if start_row > end_row else end_row
    # col_low = start_col if start_col < end_col else end_col
    # col_high = start_col if start_col > end_col else end_col

    deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    def getAllValidMoves(y0, x0):
        validPositions = []
        for (x, y) in deltas:
            xCandidate = x0 + x
            yCandidate = y0 + y
            if 0 <= xCandidate < end_col and 0 <= yCandidate < end_row:
                validPositions.append([yCandidate, xCandidate])
    
        return validPositions

    q = [(start_row, start_col, 0)]
    while q:
        row, col, level = q.pop(0)
        if row == end_row and col == end_col:
            return level

        for move in getAllValidMoves(row, col):
            # if move[1] >= row_low and move[1] <= row_high or move[0] >= col_low and move[0] <= col_high:
            q.append((move[0], move[1], level + 1))

    return -1
