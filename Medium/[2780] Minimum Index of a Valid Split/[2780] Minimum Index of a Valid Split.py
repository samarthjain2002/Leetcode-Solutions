"""
Accepted
2780 [Medium]
Runtime: 59 ms, faster than 61.88% of Python3 online submissions for Minimum Index of a Valid Split.
Memory Usage: 34.52 MB, less than 38.61% of Python3 online submissions for Minimum Index of a Valid Split.
"""
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)

        domCount = 0
        for key, val in freq.items():
            if val > domCount:
                dom = key
                domCount = val

        curCount = 0
        for i, num in enumerate(nums):
            if num == dom:
                curCount += 1
            if curCount > (i + 1) // 2 and domCount - curCount > (len(nums) - i - 1) // 2:
                return i
        return -1