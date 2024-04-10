"""
Accepted
414 [Easy]
Runtime: 51 ms, faster than 60.27% of Python3 online submissions for Third Maximum Number.
Memory Usage: 18.13 MB, less than 28.48% of Python3 online submissions for Third Maximum Number.
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) >= 3:
            return sorted(set(nums))[-3]
        else:
            return sorted(set(nums))[-1]