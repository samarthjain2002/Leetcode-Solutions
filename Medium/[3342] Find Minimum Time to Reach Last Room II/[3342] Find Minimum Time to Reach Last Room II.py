"""
Accepted
3342 [Medium]
Runtime: 1769 ms, faster than 72.53% of Python3 online submissions for Find Minimum Time to Reach Last Room II.
Memory Usage: 144.67 MB, less than 30.47% of Python3 online submissions for Find Minimum Time to Reach Last Room II.
"""
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        minHeap = [(0, 1, 0, 0)]
        visited = set([(0, 0)])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while minHeap:
            for i in range(len(minHeap)):
                time, nextStep, row, col = heapq.heappop(minHeap)
                if (row, col) == (len(moveTime) - 1, len(moveTime[0]) - 1):
                    return time

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(moveTime) and 0 <= nc < len(moveTime[0]) and (nr, nc) not in visited:
                        nStep = 1 if nextStep == 2 else 2
                        if moveTime[nr][nc] <= time:
                            heapq.heappush(minHeap, (time + nextStep, nStep, nr, nc))
                        else:
                            heapq.heappush(minHeap, (moveTime[nr][nc] + nextStep, nStep, nr, nc))
                        visited.add((nr, nc))