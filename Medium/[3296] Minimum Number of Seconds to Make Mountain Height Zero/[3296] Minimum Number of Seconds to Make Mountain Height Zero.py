"""
Accepted
3296 [Medium]
Runtime: 512 ms, faster than 29.12% of Python3 online submissions for Minimum Number of Seconds to Make Mountain Height Zero.
Memory Usage: 21.14 MB, less than 60.53% of Python3 online submissions for Minimum Number of Seconds to Make Mountain Height Zero.
"""
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        minHeap = []
        for w in workerTimes:
            heapq.heappush(minHeap, (w, w, 1))

        res = 0
        for i in range(mountainHeight):
            f, w, k = heapq.heappop(minHeap)
            res = max(res, f)
            nextF = f + (w * (k + 1))
            heapq.heappush(minHeap, (nextF, w, k + 1))
        return res