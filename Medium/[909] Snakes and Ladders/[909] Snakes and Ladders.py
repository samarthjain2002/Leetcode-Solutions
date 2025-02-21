"""
Accepted
909 [Medium]
Runtime: 39 ms, faster than 19.62% of Python3 online submissions for Snakes and Ladders.
Memory Usage: 17.99 MB, less than 59.12% of Python3 online submissions for Snakes and Ladders.
"""
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def mapper(cell):
            row = math.ceil(cell / n)
            row = abs(row - n)

            if (n % 2 and row % 2) or (n % 2 == 0 and row % 2 == 0):
                col = abs((cell % n) - n) if cell % n else 0
            else:
                col = (cell % n) - 1 if cell % n else n - 1

            return (row, col)

        queue = deque([(1, 0)])
        visited = set([1])
        while queue:
            pos, moves = queue.popleft()
            if pos == n**2:
                return moves

            for i in range(1, 7):
                nextPos = pos + i
                if nextPos > n**2:
                    break

                row, col = mapper(nextPos)
                if board[row][col] != -1:
                    nextPos = board[row][col]

                if nextPos not in visited:
                    visited.add(nextPos)
                    queue.append((nextPos, moves + 1))
        return -1