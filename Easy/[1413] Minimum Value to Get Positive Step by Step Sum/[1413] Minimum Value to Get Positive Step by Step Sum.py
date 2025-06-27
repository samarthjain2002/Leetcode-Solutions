"""
Accepted
1413 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
Memory Usage: 17.87 MB, less than 30.17% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        lowest = float("inf")
        cur = 0
        for num in nums:
            cur += num
            lowest = min(lowest, cur)

        return (lowest * -1) + 1 if lowest <= 0 else 1