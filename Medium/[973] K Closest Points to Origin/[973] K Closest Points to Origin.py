"""
Accepted
973 [Medium]
Runtime: 87 ms, faster than 26.61% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 23.65 MB, less than 5.14% of Python3 online submissions for K Closest Points to Origin.
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for x, y in points:
            ed = math.sqrt( x**2 + y**2 )
            heapq.heappush(minHeap, (ed, [x, y]))

        res = []
        for _ in range(k):
            ed, point = heapq.heappop(minHeap)
            res.append(point)
        return res