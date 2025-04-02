"""
Accepted
2873 [Easy]
Runtime: 160 ms, faster than 18.95% of Python3 online submissions for Maximum Value of an Ordered Triplet I.
Memory Usage: 17.62 MB, less than 82.79% of Python3 online submissions for Maximum Value of an Ordered Triplet I.
"""
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res