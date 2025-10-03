"""
Accepted
407 [Hard]
Runtime: 120 ms, faster than 41.43% of Python3 online submissions for Trapping Rain Water II.
Memory Usage: 26.77 MB, less than 30.19% of Python3 online submissions for Trapping Rain Water II.
"""
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])

        minHeap = []
        visited = set()
        for r in range(ROWS):
            heapq.heappush(minHeap, (heightMap[r][0], r, 0))
            visited.add((r, 0))
            heapq.heappush(minHeap, (heightMap[r][COLS - 1], r, COLS - 1))
            visited.add((r, COLS - 1))
        for c in range(COLS):
            heapq.heappush(minHeap, (heightMap[0][c], 0, c))
            visited.add((0, c))
            heapq.heappush(minHeap, (heightMap[ROWS - 1][c], ROWS - 1, c))
            visited.add((ROWS - 1, c))

        res = 0
        max_h = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while minHeap:
            h, r, c = heapq.heappop(minHeap)
            max_h = max(max_h, h)
            res += max_h - h

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    heapq.heappush(minHeap, (heightMap[nr][nc], nr, nc))
                    visited.add((nr, nc))

        return res