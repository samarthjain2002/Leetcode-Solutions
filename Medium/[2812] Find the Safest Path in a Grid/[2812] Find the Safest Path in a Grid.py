"""
Accepted
2812 [Medium]
Runtime: 5360 ms, faster than 9.54% of Python3 online submissions for Find the Safest Path in a Grid.
Memory Usage: 77.23 MB, less than 5.20% of Python3 online submissions for Find the Safest Path in a Grid.
"""
# Multi-source Breadth-First Search + Dijkstra's Solution
# TC: O(n^2 log(n)), SC: O(n^2)
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Multi-source Breadth-First Search
        queue = deque([(row, col, 0) for row in range(n) for col in range(n) if grid[row][col]])
        man_dist = {}
        while queue:
            for i in range(len(queue)):
                x, y, dist = queue.popleft()
                if (x, y) in man_dist:
                    continue
                
                man_dist[(x, y)] = dist
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in man_dist:
                        queue.append((nx, ny, dist + 1))

        # Dijkstra's algorithm
        maxHeap = [(-man_dist[(0, 0)], 0, 0)]
        visited = set()
        while maxHeap:
            safeness, r, c = heapq.heappop(maxHeap)
            if r == c == n - 1:
                return -safeness

            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # Multiply by -1 to trick the minHeap into working like a maxHeap
                    new_safeness = -1 * (min(-1 * safeness, man_dist[(nr, nc)]))
                    heapq.heappush(maxHeap, (new_safeness, nr, nc))