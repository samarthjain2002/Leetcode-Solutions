"""
Accepted
2257 [Medium]
Runtime: 301 ms, faster than 87.76% of Python3 online submissions for Count Unguarded Cells in the Grid.
Memory Usage: 39.16 MB, less than 68.37% of Python3 online submissions for Count Unguarded Cells in the Grid.
"""
# TC: O(m*n), SC: O(m*n)
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        # 0 = free, 1 = guard, 2 = wall, 3 = unguarded
        for row, col in guards:
            grid[row][col] = 1
        for row, col in walls:
            grid[row][col] = 2

        def mark_guarded(row, col):
            for c in reversed(range(0, col)):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            for c in range(col + 1, n):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3
            for r in reversed(range(0, row)):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3
            for r in range(row + 1, m):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3

        for row, col in guards:
            mark_guarded(row, col)

        res = 0
        for row in grid:
            res += row.count(0)
        return res