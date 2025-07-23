"""
Accepted
1091 [Medium]
Runtime: 287 ms, faster than 20.34% of Python3 online submissions for Shortest Path in Binary Matrix.
Memory Usage: 19.40 MB, less than 50.12% of Python3 online submissions for Shortest Path in Binary Matrix.
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), 
                        (-1, -1), (1, 1), (-1, 1), (1, -1)]
        queue = deque([(1, 0, 0)])
        visited = set()
        while queue:
            path, row, col = queue.popleft()
            if row == len(grid) - 1 and col == len(grid) - 1:
                return path

            if (row, col) in visited:
                continue
            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (0 <= nr < len(grid) and 0 <= nc < len(grid) and
                    (nr, nc) not in visited and grid[nr][nc] == 0):
                    queue.append((path + 1, nr, nc))

        return -1