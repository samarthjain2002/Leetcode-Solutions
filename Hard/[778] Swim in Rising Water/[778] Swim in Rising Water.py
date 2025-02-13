"""
Accepted
778 [Hard]
Runtime: 32 ms, faster than 48.77% of Python3 online submissions for Swim in Rising Water.
Memory Usage: 18.69 MB, less than 23.31% of Python3 online submissions for Swim in Rising Water.
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        minHeap = [(grid[0][0], 0, 0)]
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) == (ROWS - 1, COLS - 1):
                return diff

            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    newDiff = max(diff, grid[nr][nc])
                    heapq.heappush(minHeap, (newDiff, nr, nc))