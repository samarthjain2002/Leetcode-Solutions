"""
Accepted
542 [Medium]
Runtime: 147 ms, faster than 57.17% of Python3 online submissions for 01 Matrix.
Memory Usage:  20.49 MB, less than 54.59% of Python3 online submissions for 01 Matrix.
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [[float("inf")] * len(mat[0]) for _ in range(len(mat))]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    dp[i][j] = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
                    if dp[nx][ny] > dp[x][y] + 1:
                        dp[nx][ny] = dp[x][y] + 1
                        queue.append((nx, ny))

        return dp