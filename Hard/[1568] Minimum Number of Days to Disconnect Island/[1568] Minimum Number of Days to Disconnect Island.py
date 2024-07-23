"""
Accepted
1568 [Hard]
Runtime: 1396 ms, faster than 15.07% of Python3 online submissions for Minimum Number of Days to Disconnect Island.
Memory Usage: 24.33 MB, less than 8.22% of Python3 online submissions for Minimum Number of Days to Disconnect Island.
"""
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def isConnected():
            visited = set()

            def dfs(i, j):
                if (i, j) in visited or i == -1 or i == M or j == -1 or j == N or grid[i][j] == 0:
                    return
                visited.add((i,j))
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)

            for i in range(M):
                for j in range(N):
                    if grid[i][j]:
                        dfs(i,j)
                        break
                if visited:
                    break
            
            if not visited:     # For testcase where no land is found
                return False

            for i in range(M):
                for j in range(N):
                    if grid[i][j] and (i,j) not in visited:
                        return False
            return True

        if not isConnected():     # There are multiple islands
            return 0

        # Step 2: Try changing one land cell to water and check if it disconnects the grid
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not isConnected():
                        grid[i][j] = 1  # Revert the change
                        return 1
                    grid[i][j] = 1  # Revert the change

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    for x in range(M):
                        for y in range(N):
                            if grid[x][y] == 1:
                                grid[x][y] = 0
                                if not isConnected():
                                    grid[x][y] = 1  # Revert the change
                                    grid[i][j] = 1  # Revert the change
                                    return 2
                                grid[x][y] = 1  # Revert the change
                    grid[i][j] = 1  # Revert the change

        return 2