"""
Accepted
2348 [Easy]
Runtime: 32 ms, faster than 68.93% of Python3 online submissions for Number of Zero-Filled Subarrays.
Memory Usage: 33.66 MB, less than 52.32% of Python3 online submissions for Number of Zero-Filled Subarrays.
"""
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums.append(1)
        count = 0
        res = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                res += (count**2 + count) // 2
                count = 0
        return res