"""
Accepted
128 [Medium]
Runtime: 4013 ms, faster than 34.51% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage:  31.88 MB, less than 69.91% of Python3 online submissions for Longest Consecutive Sequence.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in numSet:
                length = 0
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)

        return longest