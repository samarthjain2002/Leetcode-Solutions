"""
Accepted
594 [Easy]
Runtime: 36 ms, faster than 96.22% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 16.76 MB, less than 6.46% of Python3 online submissions for Longest Harmonious Subsequence.
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for num in nums:
            if num in freq and num + 1 in freq:
                res = max(res, freq[num] + freq[num + 1])
        return res