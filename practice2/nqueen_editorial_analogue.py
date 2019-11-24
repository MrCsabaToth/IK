QUEEN = "q"
NO_QUEEN = "-"

def find_all_arrangements(n):
    result = []
    diagf = [False] * (2 * n -1)  # forward diagonal
    diagb = [False] * (2 * n -1)  # backward diagonal
    col_indicator = [False] * n

    def q_helper(partial_board, row):
        if row == n:
            solution = ["".join(x) for x in partial_board]
            if solution not in result:
                result.append(solution)

            return

        for col in range(n):
            if col_indicator[col] or diagf[col + row] or diagb[col - row + n - 1]:
                continue

            partial_board[row][col] = QUEEN
            col_indicator[col] = True
            diagf[col + row] = True
            diagb[col - row + n - 1] = True

            q_helper(partial_board, row + 1)

            diagb[col - row + n - 1] = False
            diagf[col + row] = False
            col_indicator[col] = False
            partial_board[row][col] = NO_QUEEN

    curr_board = [[NO_QUEEN] * n for _ in range(n)]
    q_helper(curr_board, 0)

    return result
