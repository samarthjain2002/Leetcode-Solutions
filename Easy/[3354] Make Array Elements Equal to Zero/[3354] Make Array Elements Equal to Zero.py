"""
Accepted
3354 [Easy]
Runtime: 50 ms, faster than 47.34% of Python3 online submissions for Make Array Elements Equal to Zero.
Memory Usage: 17.74 MB, less than 54.26% of Python3 online submissions for Make Array Elements Equal to Zero.
"""
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefixSums = [0] * len(nums)
        prefixSums[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSums[i] = prefixSums[i - 1] + nums[i]

        res = 0
        for i in range(len(prefixSums)):
            if nums[i] == 0:
                left, right = prefixSums[i], prefixSums[-1] - prefixSums[i]
                if left == right:
                    res += 2
                elif left + 1 == right or left == right + 1:
                    res += 1
        return res