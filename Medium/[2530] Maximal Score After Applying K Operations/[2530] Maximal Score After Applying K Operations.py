"""
Accepted
2530 [Medium]
Runtime: 723 ms, faster than 62.34% of Python3 online submissions for Maximal Score After Applying K Operations.
Memory Usage: 31.38 MB, less than 20.57% of Python3 online submissions for Maximal Score After Applying K Operations.
"""
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            score = heapq.heappop(nums) * -1
            res += score
            heapq.heappush(nums, -1 * math.ceil(score / 3))
        return res