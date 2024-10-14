"""
Accepted
1962 [Medium]
Runtime: 1249 ms, faster than 75.09% of Python3 online submissions for Remove Stones to Minimize the Total.
Memory Usage: 31.32 MB, less than 53.83% of Python3 online submissions for Remove Stones to Minimize the Total.
"""
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        for i in range(k):
            score = heapq.heappop(piles) * -1
            heapq.heappush(piles, -1 * score // 2)
        return sum(piles) * -1