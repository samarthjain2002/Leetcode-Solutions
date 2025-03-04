"""
Accepted
1765 [Medium]
Runtime: 1007 ms, faster than 55.29% of Python3 online submissions for Map of Highest Peak.
Memory Usage: 84.90 MB, less than 53.88% of Python3 online submissions for Map of Highest Peak.
"""
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dp = [[float("inf")] * len(isWater[0]) for _ in range(len(isWater))]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = deque()

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    dp[i][j] = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(isWater) and 0 <= ny < len(isWater[0]):
                    if dp[nx][ny] > dp[x][y] + 1:
                        dp[nx][ny] = dp[x][y] + 1
                        queue.append((nx, ny))

        return dp