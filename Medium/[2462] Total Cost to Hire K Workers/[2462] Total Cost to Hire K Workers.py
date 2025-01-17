"""
Accepted
2462 [Medium]
Runtime: 239 ms, faster than 31.46% of Python3 online submissions for Total Cost to Hire K Workers.
Memory Usage: 35.93 MB, less than 5.90% of Python3 online submissions for Total Cost to Hire K Workers.
"""
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        minHeap = []

        left, right = 0, len(costs) - 1
        for i in range(candidates):
            if left <= right:
                heapq.heappush(minHeap, (costs[i], left))
                left += 1
            if left <= right:
                heapq.heappush(minHeap, (costs[right], right))
                right -= 1

        totalCost = 0
        for _ in range(k):
            cost, index = heapq.heappop(minHeap)
            totalCost += cost
            if left <= right:
                if index < left:
                    heapq.heappush(minHeap, (costs[left], left))
                    left += 1
                else:
                    heapq.heappush(minHeap, (costs[right], right))
                    right -= 1
        return totalCost