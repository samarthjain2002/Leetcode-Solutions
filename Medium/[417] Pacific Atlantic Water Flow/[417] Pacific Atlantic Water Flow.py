"""
Accepted
417 [Medium]
Runtime: 47 ms, faster than 28.58% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 19.38 MB, less than 16.56% of Python3 online submissions for Pacific Atlantic Water Flow.
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        pac, atl = set(), set()

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(row, col, h, ocean):
            if row == -1 or row == len(heights) or col == -1 or col == len(heights[0]) or (row, col) in ocean or heights[row][col] < h:
                return

            ocean.add((row, col))
            for dx, dy in directions:
                dfs(row + dx, col + dy, heights[row][col], ocean)

        for col in range(N):
            dfs(0, col, -1, pac)
            dfs(len(heights) - 1, col, -1, atl)
        for row in range(M):
            dfs(row, 0, -1, pac)
            dfs(row, len(heights[0]) - 1, -1, atl)

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res