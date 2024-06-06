"""
Accepted
228 [Easy]
Runtime: 35 ms, faster than 51.23% of Python3 online submissions for Summary Ranges.
Memory Usage: 65.56 MB, less than 39.93% of Python3 online submissions for Summary Ranges.
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        res = []
        for right, num in enumerate(nums):
            if num != nums[left] + right - left:
                if right == left + 1:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left]) + "->" + str(nums[right - 1]))
                left = right
        if left < len(nums):
            if left == len(nums) - 1:
                res.append(str(nums[left]))
            else:
                res.append(str(nums[left]) + "->" + str(nums[-1]))
        return res