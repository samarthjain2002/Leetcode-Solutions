"""
Accepted
1584 [Medium]
Runtime: 2028 ms, faster than 34.64% of Python3 online submissions for Min Cost to Connect All Points.
Memory Usage: 16.53 MB, less than 51.83% of Python3 online submissions for Min Cost to Connect All Points.
"""
# Prim's Algorithm
# TC: O(n^2 log(n)), SC: O(n^2)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # Building the adjacency map (point1: [[dist1, point2], ...])
        adjMap = defaultdict(list)
        for point1 in range(N):
            x1, y1 = points[point1]
            for point2 in range(point1 + 1, N):
                x2, y2 = points[point2]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjMap[point1].append([dist, point2])
                adjMap[point2].append([dist, point1])

        
        # Prim's algorithm
        res = 0
        visited = set()
        minHeap = [(0, 0)]
        while len(visited) < N:
            weight, point = heapq.heappop(minHeap)

            if point in visited:
                continue
            visited.add(point)
            res += weight

            for neiWeight, nei in adjMap[point]:
                if nei not in visited:
                    heapq.heappush(minHeap, (neiWeight, nei))
        return res