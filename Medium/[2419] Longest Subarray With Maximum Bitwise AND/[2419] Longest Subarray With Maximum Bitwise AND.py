"""
Accepted
2419 [Medium]
Runtime: 637 ms, faster than 73.09% of Python3 online submissions for Longest Subarray With Maximum Bitwise AND.
Memory Usage: 30.94 MB, less than 70.91% of Python3 online submissions for Longest Subarray With Maximum Bitwise AND.
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        m = max(nums)
        i = 0
        res = 0
        while i < N:
            if nums[i] == m:
                count = 0
                for j in range(i, N):
                    if nums[j] == m:
                        count += 1
                    else:
                        break
                res = max(res, count)
                i = j
            i += 1
        return res