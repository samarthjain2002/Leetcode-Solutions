"""
Accepted
1004 [Medium]
Runtime: 454 ms, faster than 33.64% of Python online submissions for Max Consecutive Ones III.
Memory Usage: 16.90 MB, less than 99.48% of Python online submissions for Max Consecutive Ones III.
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        count, res = 0, 0
        for right in range(N):
            if nums[right] == 0:
                if k > 0:
                    count += 1
                    k -= 1
                else:
                    while nums[left] != 0 and left < right:
                        left += 1
                    left += 1
                    count = right - left + 1
            else:
                count += 1
            res = max(res, count)
        return res