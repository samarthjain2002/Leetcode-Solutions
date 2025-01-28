"""
Accepted
2658 [Medium]
Runtime: 77 ms, faster than 11.71% of Python online submissions for Maximum Number of Fish in a Grid.
Memory Usage: 18.18 MB, less than 18.78% of Python online submissions for Maximum Number of Fish in a Grid.
"""
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(x, y):
            if x in [-1, len(grid)] or y in [-1, len(grid[0])] or grid[x][y] == 0 or (x, y) in visited:
                return 0

            visited.add((x, y))
            return grid[x][y] + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x + 1, y) + dfs(x, y - 1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited:
                    res = max(res, dfs(r, c))
        return res