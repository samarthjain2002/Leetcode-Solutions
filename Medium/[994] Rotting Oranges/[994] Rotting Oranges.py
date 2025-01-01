"""
Accepted
994 [Medium]
Runtime: 6 ms, faster than 33.26% of Python3 online submissions for Rotting Oranges.
Memory Usage: 17.85 MB, less than 9.46% of Python3 online submissions for Rotting Oranges.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        time = fresh = 0
        queue = deque()
        for row in range(M):
            for col in range(N):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
                    
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue and fresh:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dx, dy in directions:
                    r, c = row + dx, col + dy
                    if r == -1 or r == M or c == -1 or c == N or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    queue.append((r, c))
                    fresh -= 1
            time += 1
            
        return -1 if fresh else time