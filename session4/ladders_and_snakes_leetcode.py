class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Generate board
        N = len(board)
        target = N * N
        n = target + 1
        adj_list = dict()
        for i in range(target):
            adj_list[i] = []
            for j in range(1, 7):
                pos = i + j - 1
                if pos >= target:
                    continue

                # reverse board (top to bottom)
                y_inv = pos // N
                y = N - 1 - y_inv
                # zig-zag
                even = y_inv % 2 == 0
                x = pos % N
                if not even:
                    x = N - 1 - x

                vertex = pos + 1 if board[y][x] == -1 else board[y][x]
                if vertex not in adj_list[i]:
                    adj_list[i].append(vertex)

        q = [(0, 0, [0])]
        while q:
            node, moves, visited = q.pop(0)
            if node == target:
                return moves

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    q.append((neighbor, moves + 1, visited + [neighbor]))

        return -1
