"""
Accepted
3341 [Medium]
Runtime: 119 ms, faster than 89.37% of Python3 online submissions for Find Minimum Time to Reach Last Room I.
Memory Usage: 18.52 MB, less than 28.07% of Python3 online submissions for Find Minimum Time to Reach Last Room I.
"""
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        minHeap = [(0, 0, 0)]
        visited = set([(0, 0)])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while minHeap:
            for i in range(len(minHeap)):
                time, row, col = heapq.heappop(minHeap)
                if (row, col) == (len(moveTime) - 1, len(moveTime[0]) - 1):
                    return time

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(moveTime) and 0 <= nc < len(moveTime[0]) and (nr, nc) not in visited:
                        if moveTime[nr][nc] <= time:
                            heapq.heappush(minHeap, (time + 1, nr, nc))
                        else:
                            heapq.heappush(minHeap, (moveTime[nr][nc] + 1, nr, nc))
                        visited.add((nr, nc))