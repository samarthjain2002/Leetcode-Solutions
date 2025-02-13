"""
Accepted
1631 [Medium]
Runtime: 309 ms, faster than 70.30% of Python3 online submissions for Path With Minimum Effort.
Memory Usage: 20.22 MB, less than 30.41% of Python3 online submissions for Path With Minimum Effort.
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        minHeap = [(0, 0, 0)]
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if (r, c) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    newDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(minHeap, (newDiff, nr, nc))