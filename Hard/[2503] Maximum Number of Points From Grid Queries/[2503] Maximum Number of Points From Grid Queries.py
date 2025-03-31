"""
Accepted
2503 [Hard]
Runtime: 633 ms, faster than 58.68% of Python3 online submissions for Maximum Number of Points From Grid Queries.
Memory Usage: 42.87 MB, less than 19.84% of Python3 online submissions for Maximum Number of Points From Grid Queries.
"""
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()

        res = [0] * len(queries)
        minHeap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        points = 0

        for limit, index in q:
            while minHeap and minHeap[0][0] < limit:
                val, r, c = heappop(minHeap)
                points += 1
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and 0 <= nc < COLS and
                        (nr, nc) not in visited
                    ):
                        heappush(minHeap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            res[index] = points
        return res