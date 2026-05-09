"""
Accepted
1914 [Medium]
Runtime: 121 ms, faster than 32.86% of Python3 online submissions for Cyclically Rotating a Grid.
Memory Usage: 19.74 MB, less than 21.43% of Python3 online submissions for Cyclically Rotating a Grid.
"""
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m // 2, n // 2)

        res = [[0] * n for _ in range(m)]

        for i in range(layers):
            queue = deque()
            for j in range(i, n - i):
                queue.append(grid[i][j])
            for j in range(i + 1, m - i - 1):
                queue.append(grid[j][n - 1 - i])
            for j in range(n - 1 - i, i - 1, -1):
                queue.append(grid[m - 1 - i][j])
            for j in range(m - 1 - i - 1, i - 1 + 1, -1):
                queue.append(grid[j][i])

            newK = k % len(queue)
            for _ in range(newK):
                queue.append(queue.popleft())

            pointer = 0
            for j in range(i, n - i):
                res[i][j] = queue[pointer]
                pointer += 1
            for j in range(i + 1, m - i - 1):
                res[j][n - 1 - i] = queue[pointer]
                pointer += 1
            for j in range(n - 1 - i, i - 1, -1):
                res[m - 1 - i][j] = queue[pointer]
                pointer += 1
            for j in range(m - 1 - i - 1, i - 1 + 1, -1):
                res[j][i] = queue[pointer]
                pointer += 1

        return res