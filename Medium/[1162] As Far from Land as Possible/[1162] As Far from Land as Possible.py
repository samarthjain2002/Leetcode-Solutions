"""
Accepted
1162 [Medium]
Runtime: 186 ms, faster than 46.70% of Python3 online submissions for As Far from Land as Possible.
Memory Usage: 19.73 MB, less than 41.15% of Python3 online submissions for As Far from Land as Possible.
"""
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)

        queue = deque([(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val])
        if not queue or len(queue) == N * N:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
        res = -1
        visited = set()
        while queue:
            res += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < N and 0 <= nc < N and
                         (nr, nc) not in visited and grid[nr][nc] != 1):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        return res