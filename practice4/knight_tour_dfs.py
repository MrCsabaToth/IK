def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    min_steps = -1

    row_low = start_row if start_row < end_row else end_row
    row_high = start_row if start_row > end_row else end_row
    row_dist = row_high - row_low
    col_low = start_col if start_col < end_col else end_col
    col_high = start_col if start_col > end_col else end_col
    col_dist = col_high - col_low
    import math
    max_moves = int(math.sqrt(row_dist ** 2 + col_dist ** 2) * 0.7 + 0.5 + 2)

    deltas = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    def getAllValidMoves(y0, x0):
        validPositions = []
        for (x, y) in deltas:
            xCandidate = x0 + x
            yCandidate = y0 + y
            if 0 <= xCandidate < end_col and 0 <= yCandidate < end_row:
                validPositions.append([yCandidate, xCandidate])
    
        return validPositions

    def dfs(row, col, level):
        if row == end_row and col == end_col:
            if level < min_steps or min_steps == -1:
                min_steps = level

            return

        if level > max_moves:
            return

        for move in getAllValidMoves(row, col):
            if move[1] >= row_low and move[1] <= row_high or move[0] >= col_low and move[0] <= col_high:
                dfs(move[0], move[1], level + 1)

    dfs(start_row, end_row, 0)
    return min_steps
