"""
Accepted
3446 [Medium]
Runtime: 3 ms, faster than 98.75% of Python3 online submissions for Sort Matrix by Diagonals.
Memory Usage: 17.74 MB, less than 82.92% of Python3 online submissions for Sort Matrix by Diagonals.
"""
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)

        for col in range(N - 1, 0, -1):
            i, j = 0, col
            diag = []
            while j < N:
                diag.append(grid[i][j])
                i += 1
                j += 1

            diag.sort()

            i, j = 0, col
            while j < N:
                grid[i][j] = diag[i]
                i += 1
                j += 1

        for row in range(N):
            i, j = row, 0
            diag = []
            while i < N:
                diag.append(grid[i][j])
                i += 1
                j += 1

            diag.sort()
            diag.reverse()

            i, j = row, 0
            while i < N:
                grid[i][j] = diag[j]
                i += 1
                j += 1

        return grid