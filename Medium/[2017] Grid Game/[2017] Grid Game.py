"""
Accepted
2017 [Medium]
Runtime: 148 ms, faster than 12.13% of Python3 online submissions for Maximum Matrix Sum.
Memory Usage: 29.60 MB, less than 62.95% of Python3 online submissions for Maximum Matrix Sum.
"""
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefixSums = grid.copy()
        for j in range(1, len(grid[0])):
            prefixSums[0][j] = prefixSums[0][j] + prefixSums[0][j - 1]
            prefixSums[1][j] = prefixSums[1][j] + prefixSums[1][j - 1]

        res = float("inf")
        for j in range(len(grid[0])):
            top = prefixSums[0][-1] - prefixSums[0][j]
            bottom = prefixSums[1][j - 1] if j > 0 else 0
            secondRobot = max(top, bottom)
            res = min(res, secondRobot)
        return res