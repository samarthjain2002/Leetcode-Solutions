"""
Accepted
3286 [Medium]
Runtime: 63 ms, faster than 83.49% of Python3 online submissions for Find a Safe Walk Through a Grid.
Memory Usage: 20.14 MB, less than 27.36% of Python3 online submissions for Find a Safe Walk Through a Grid.
"""
# 0-1 Breadth-First Search Solution
# TC: O(mn), SC: O(mn)
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        queue = deque([(grid[0][0], 0, 0)])
        visited = set()
        while queue:
            damage, r, c = queue.popleft()

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if damage >= health:
                return False
            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc]:    # Push it to the end of queue
                        queue.append((damage + 1, nr, nc))
                    else:               # Prepend the cell to queue
                        queue.appendleft((damage, nr, nc))



"""
Runtime: 155 ms, faster than 48.11% of Python3 online submissions for Find a Safe Walk Through a Grid.
Memory Usage: 20.14 MB, less than 27.36% of Python3 online submissions for Find a Safe Walk Through a Grid.
"""
# Dijkstra's algorithm Solution
# TC: O(mnlog(mn)), SC: O(mn)
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        maxHeap = [(-(health - grid[0][0]), 0, 0)]
        visited = set()
        while maxHeap:
            health, r, c = heapq.heappop(maxHeap)
            health = -health
            if health <= 0:
                return False
            if r == m - 1 and c == n - 1:
                return True

            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc]:
                        heapq.heappush(maxHeap, (-(health - 1), nr, nc))
                    else:
                        heapq.heappush(maxHeap, (-health, nr, nc))